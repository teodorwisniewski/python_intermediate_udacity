# Meme Generator project
> This simple Flask API can generate memes with random quotes.
The app combines predefined images with several quotes in order to generate memes. 


## About the project

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes. You could manually copy and paste these quotes into one standard format – but you’re going to over-engineer a solution to load quotes from each file to show off your fancy new Python skills.

## Python Modules
The Quote Engine module is responsible for ingesting many types of files that contain quotes. 
For our purposes, a quote contains a body and an author. This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.
The ingestors can be found in the following directory:
```sh
MemeEngine:
    -> __init__.py
    -> Ingestor.py
    -> CSVIngestor.py
    -> DOCXIngestor.py
    -> PDFIngestor.py
    -> QuoteModel.py
    -> IngestorInterface.py
```
Four formats have been defined: csv, docx, txt and pdf. It can be futher devolopped for other formats. One has to use
IngestorInterface.py abstract class for that purpose. The `Ingestor.py` allows to use them all at once.



## Installation
FYI: The code requires Python 3.8 to run.
On Windows:
```sh
pip install -r requirements.txt
```
On Linux:
```sh
pip3 install -r requirements.txt
```

## Running Flask APP
On Windows:
```sh
python app.py
```
On Linux:
```sh
python3 app.py
```

## Running tests
Unit tests are in the _tests_ directory and can be run with unittest python library:
```sh
python -m unittest --verbose
```
On Linux:
```sh
python3 -m unittest --verbose
```


## Output example

The following result can be obtained with the Meme Generator: <br>
![Meme Example](./static/example.jpg)


## Author
Teodor Wisniewski and Udacity

