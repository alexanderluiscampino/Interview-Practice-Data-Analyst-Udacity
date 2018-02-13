# P7: Interview Practice - Data Analyst - Udacity
This readme file will serve to answer the Project Submission for the 
interview Practice of Udacity's Data Analyst Nanodegree.  


### Question 1 - Describe a data project you worked on recently.

I have been working recently in merging and analyzing my company’s
sales/user data. This is a two part work. At the moment, the data is 
spread across 7 different web tools, most of them are outdated. 
So I have been writing Python routines to scrap and mine this data. 
Unfortunately most of these tools do not have a easy output, so 
scraping from the HTML file has been the solution, for the most part.
After all this data is mined/gathered into a database, using csv files 
for the first part, it is cleaned using Pandas. Data is then stored in 
a SQL database, so it can readily be used in the future. 
The second part of the project is the Data Analytics and presentation. 
I am using Tableau and R language to read the SQL database and build models
to predict the outcome of our events. 
Also with Tableau, I make weekly visualizations about the past week’s numbers,
organized in a neat way which allows the company to draw conclusions and plan
events better. All this work has already given fruits, since we reduced our
wasted materials billing in 30%. Also we have steadily been increasing our
revenue each month, by 5%, due to the models that are now in place.


### Question 2 - You are given a ten piece box of chocolate truffles.

You know based on the label that six of the pieces have an orange cream 
filling and four of the pieces have a coconut filling. If you were to eat 
four pieces in a row, what is the probability that the first two pieces 
you eat have an orange cream filling and the last two have a coconut
filling?

Great way to answer this question is using a tree diagram. 
Let's call P(A) the probability of occurring the event in question. 
P(O) is the probability of eating a Orange filling and P(C) a coconut filling.
We only have one type of event order that matters. Which is:
	P(O) -> P(O) -> P(C) -> P(C)
On the first chocolate we have P(O) = 6/10, 2nd is 5/9. Then P(C) is 4/8=½
and then 3/7. All this probabilities are independent so we can 
just calculate P(A) = 6/10 x 5/9 x ½ x 3/7 = 1/14 = 0.0714 or 7%


 Ate    | Probability | O left | C left 
--------|-------------|------------|-------------
 -      |      -      | 6          | 4
 O      | 6/10        | 5          | 4
 O      | 5/9         | 4          | 4
 C      | 1/2         | 4          | 3
 C      | 3/7         | 4          | 2
 
Total:

```
0.6 * 5/9 * 0.5 * 3/7 = 0.07
```

### Follow up question:

If you were given an identical box of chocolates and again eat four 
pieces in a row, what is the probability that exactly two contain 
coconut filling?

There are 6 different possible order of events that allow us to eat exactly 2
Coconut chocolates. These are:

C C O O
O C C O
O O C C
C O O C
C O C O
O C O C

It is possible to calculate the probabilite of each individual event,
and then add them up in the end. The following python code achieves
the intended: 

```python
import operator


def eat_one_piece(box, choco):
    """
    Determines the probability of eating a certain
    type of chocolate
    :param chocolate_box: dict of {type: count}.
    :return (float, chocolate_box): probability and updated box.
    """
    total_chocos = sum(chocolate_box.values())
    prob = (0. + chocolate_box[choco]) / total_choco
    if chocolate_box[choco]:
        chocolate_box[choco] -= 1
    return prob, chocolate_box


def order_event(chocolate_box, seq):
    """Determines probability of order of chocos.
    :param chocolate_box: dict of {type: count}.
    :param seq: string
    :return float
    """
    prob = []
    for choco in seq:
        p, chocolate_box = eat_one_piece(chocolate_box, choco)
        prob.append(p)
    return reduce(operator.mul, prob, 1)


if __name__ == '__main__':
    total_prob = 0
    for seq in ['CCOO', 'OCCO', 'OOCC', 'COOC', 'COCO', 'OCOC']:
        chocolate_box = {'O': 6, 'C': 4}
        ps = order_event(box, seq)
        print '- {}: {}'.format(seq, ps)
        total_prob += ps
    print 'Result', total_prob
```

Here is the output:

```
- CCOO: 0.0714285714286
- OCCO: 0.0714285714286
- OOCC: 0.0714285714286
- COOC: 0.0714285714286
- COCO: 0.0714285714286
- OCOC: 0.0714285714286
Result 0.428571428571
```

### Question 3 - Given the table users:

        Table "users"        
| Column      | Type      |
|-------------|-----------|
| id          | integer   |
| username    | character |
| email       | character |
| city        | character |
| state       | character |
| zip         | integer   |
| active      | boolean   |

construct a query to find the top 5 states with the highest number of 
active users. Include the number for each state in the query result.
Example result:

| state      | num_active_users |
|------------|------------------|
| New Mexico | 502              |
| Alabama    | 495              |
| California | 300              |
| Maine      | 201              |
| Texas      | 189              |

The following SQL command will do the intended:

```sql
select state, count(id) as num_active_users from users
where active = 1
group by state
order by num_active_users desc
limit 5
```

### Question 4 - Define a function first_unique

that takes a string as input and returns the first non-repeated (unique)
character in the input string. If there are no unique characters return
None. Note: Your code should be in Python.

```
def first_unique(string):
    # Your code here
    return unique_char

> first_unique('aabbcdd123')
> c

> first_unique('a')
> a

> first_unique('112233')
> None
```

```python
def first_unique(string):
    if string.upper().isupper(): # if it has letters
        if len(string) == 1:
            return string
        else:
            letter = {}
            for index,char in enumerate(string):
                if letter.get(char) == None:
                    letter[char] = [1,index]
                else:
                    letter[char] = [letter[char][0]+1,index]
            print(letter)

    else:
        return None





print(first_unique('aabbcdd123'))
```

```python
def first_unique(string):
    seen = set([])
    for i in range(len(string)):
        letter = string[i]
        if letter not in seen and letter not in string[i+1:]:
            return letter
        seen.add(letter)
    return None

```

This solution is short to code and easy to understand. However,
complexity is O(N^2), since we are doing the look-ahead through the 
string for every letter, slightly mitigating it by the `seen` check.
It may be more efficient to:

* create a dict of `letter: (count, index)`: O(N)
* loop through the dict and find key with count=1 and minimal index: O(N)

Here, complexity would be O(2*N).

### Question 5 - What are underfitting and overfitting

in the context of Machine Learning? How might you balance them?

Underfitting is the situation when the model does not capture the trend in
data well, i.e. even on training set, performance is not good. Overfitting
is when the model shows good results on training set, but poor results on 
new data. Validation and cross-validation of the model are the usual ways
to fix it.

Possible causes of underfitting:

* model is too simple
* not enough features
* bad choice of parameters

Possible causes of overfitting:

* too few data points
* too many features
* data has noise

Before answering the final question, insert a job description for a 
data analyst position of your choice!

Your answer for Question 6 should be targeted to the company/job-description you chose.

### Question 6 - If you were to start your data analyst position today,

what would be your goals a year from now?

Job description (http://www.parsely.com/jobs/#software_engineer):

```
Software Engineer

We are hiring a software engineer to work on our real-time analytics 
dashboard. Pythonistas and JavaScript hackers especially desired.

Our analytics platform helps digital storytellers at some of the web's 
best sites, such as Arstechnica, New Yorker, Mashable, The Next Web, 
and many more. In total, our analytics backend system needs to 
handle over 50 billion monthly events from over 475 million monthly 
unique visitors.

We are currently looking for software engineers to help us build the 
best real-time analytics dashboard the world has ever seen. The only 
requirement is some experience in Python/JavaScript. Bonus points for 
an interest in information visualization, Edward Tufte, and d3.js. 
To see an example of how we work, check out the blog post, "Whatever It Takes".

Responsibilities

Write code using the best practices.
Analyze data at massive scale.
Brainstorm new product ideas and directions with team and customers.
Master cloud technologies and systems.
Learn, grow, and succeed in your career.

Requirements

Ideally 2-3 years experience in technology, but no minimum experience required.
Self-sufficient, but works well with others.
Highly organized and disciplined about self-improvement.
Open source contributions and publicly scrutable code available.
Some background in Python and/or JavaScript.

```

(I got this job description from my current company jobs page, because
right now I'm happy with my job).

A year from now, I'd like to:

1. Be able to efficiently use Apache Spark and Apache Storm in my work.

How I might achieve that:

* Learn from existing code.
* Use technical documentation.
* Ask questions from more experienced team members.

Those two systems are the foundation of our current data processing
pipeline. We make it work, but problems still come up, and currently
we spend about 20% of development time (1 day every week) on fixing
customer issues that could be prevented if we increased stability and
reliability of the system. I would call it a win if we could cut this
time in half and only need to have a "bug day" once every two weeks.

2. Become an expert in monitoring tools and create a single dashboard
that we can use to diagnose problems arising during the daily data
processing tasks. Use it to determine the bottlenecks and parts of the
pipeline that have problems most often, and potentially would prevent
us from scaling the system to support more events.
