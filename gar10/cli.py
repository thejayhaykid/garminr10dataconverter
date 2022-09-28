""" CLI for Data Converter """

import click
import os
import r10_data_converter


@click.command()
@click.option(
    "--input",
    "-i",
    default="",
    required=False,
    prompt="Input path to folder. Leave blank to use current folder.",
    help="The input folder, must be downloaded from Garmin. Leave blank to use current folder.",
)
@click.option(
    "--output",
    "-o",
    default="",
    required=False,
    prompt="Output file location. Leave blank to use current folder.",
    help="The output folder. Leave blank to use current folder.",
)
def main(input, output):
    input_path = os.path.curdir
    output_path = os.path.curdir

    if (input.length > 0):
        input_path = os.path.normpath(input)
    if (output.length > 0):
        output_path = os.path.normpath(output)
    path = os.path.join(input_path, "DI_CONNECT", "DI-GOLF")
    converter = r10_data_converter.GAR10Converter()
    converter.convert(input_path=path, output_file_path=output_path)
