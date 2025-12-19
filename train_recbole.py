from recbole.quick_start import run_recbole
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_name", type=str, default="EASE")
    model_name = parser.parse_args().model_name

    run_recbole(
        model=model_name,
        dataset="my_dataset",
        config_file_list=f'{model_name.lower()}_config.yaml'
    )