import sys
import pathlib
import argparse
import pandas as pd

from testaug.testaug import generate_gpt3_test_suite
from termcolor import cprint
from utils.data import load_checklist
from utils.common import (
    get_system_time,
    seed_everything,
    load_pickle_file
)

from setting import setting

seed_everything(42)

parser = argparse.ArgumentParser()
parser.add_argument("--task", choices=["sentiment", "qqp", "nli"])
parser.add_argument("--description", type=int)
parser.add_argument("--size", type=int, default=400)
args = parser.parse_args()

task = args.task
task = "sentiment"
args.description = 3
# sentiment

desc_dict = load_pickle_file(
    setting.data_base_path / pathlib.Path(f"config/{task}.pkl"))
index = None if args.description is None else str(args.description).zfill(3)

test_path = setting.data_base_path / pathlib.Path(f"test/{task}")
test_path.mkdir(parents=True, exist_ok=True)

# T = load_checklist(task=task, keep_pool=True)
# print("T")
# print(T)
d = {'capability': ["capability_1"],
    'description': ["description_1"],
    'template': ["template_1"], 
    'label':[1],
    'text':["Did I hate that aircraft?"]
    }
columns = ['capability', 'description', 'template', 'label', 'text']
T = pd.DataFrame( columns=columns, data=d)

for idx, desc in desc_dict.items():
    if index is not None and idx != index:
        continue

    seed_df = T[T.description == desc]
    n_unique_template = seed_df.template.nunique()
    n_unique_template = 1


    cprint(desc, "red")
    df = generate_gpt3_test_suite(
        seed_df,
        task=task,
        model="text-davinci-001",
        n_demonstration=3,
        n_per_query=10,
        n_test_case_per_template=int(args.size / n_unique_template)
    )
    df.to_pickle(test_path / "{}@{}.pkl".format(idx, get_system_time()))