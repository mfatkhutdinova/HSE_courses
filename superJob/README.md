# SuperJob
#### In this project, we take the data and programmers from Moscow. Use the website SuperJob. Looking for programmers C, C++, C#, Java, Python , etc., and consider them to be average salary. Next, build the graph on this data.

## superJob_api.py 
File allows you to data from "SuperJob". You must [register](https://www.superjob.ru) on the website and obtain an API key. This requires an API key. 
Look at the [documentation](https://api.superjob.ru). 

## programmer.py
Collects the programmers on the website and puts them in *.json.

## useful_info_programmer.py
Data processing. The script accepts a file from the previous paragraph and generates another json file.
It is only useful information: the name, salary and job requirements.

## rating_languages.py
Statistics for different programming languages. For each programming language displays the number of jobs and average salary. 
All this is displayed using a histogram.
If the applicant did not specify salary, I didn't think this job is relevant. 
In consequence of this, some programming languages in the histogram are not displayed because their number is equal to 0 or the applicant has not a salary.

## graphics.py
Draws a histogram.

