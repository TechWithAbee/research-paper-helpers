In this repository I will write some helper scripts to automate the process of writing research papers.

For example:

`order.py` - this script will order the citations in the square brackets in the correct order.

I faced some issues with the citation order in the past, so I decided to write this script to automate the process.

Given the following citations:

```
[27, 40, 41, 33, 34, 48, 35,38, 49, 39, 47] 
```

We can also manually order the citations. But what if we have a list of tons of citations? It will be a nightmare to order them manually.

So, run the script and it will order the citations for you.

```
python3 order.py paper.txt paper_ordered.txt
```

The script will read the citations from `paper.txt` and write the ordered citations to `paper_ordered.txt`.

Result:

```
[27, 33, 34, 35, 38, 39, 40, 41, 47, 48, 49]
```

Should you have any questions, feedbacks and suggestions. Message me abdibrokhim@gmail.com.