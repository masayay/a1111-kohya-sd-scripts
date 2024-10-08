import gradio as gr

from scripts import ui
from scripts.runner import initialize_runner
from scripts.utilities import load_args_template, options_to_gradio


def title():
    return "Check lora weights"


def create_ui():
    options = {}
    templates, script_file = load_args_template("networks", "check_lora_weights.py")

    with gr.Column():
        init = initialize_runner(script_file, templates, options)
        with gr.Box():
            ui.title("Options")
            with gr.Column():
                options_to_gradio(templates, options)

    init()
