import gradio as gr

from scripts import presets, ui
from scripts.runner import initialize_runner
from scripts.utilities import load_args_template, options_to_gradio


def title():
    return "Tag images by wd1.4tagger"


def create_ui():
    options = {}
    templates, script_file = load_args_template(
        "finetune", "tag_images_by_wd14_tagger.py"
    )

    with gr.Column():
        init_runner = initialize_runner(script_file, templates, options)
        with gr.Box():
            with gr.Row():
                init_id = presets.create_ui(
                    "finetune.tag_images_by_wd14_tagger", templates, options
                )
        with gr.Box():
            ui.title("Options")
            with gr.Column():
                options_to_gradio(templates, options)

    init_runner()
    init_id()
