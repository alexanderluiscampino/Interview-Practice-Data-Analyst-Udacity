# Interview Practice - Data Analyst - Udacity
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
With this project I have learned quite in depth exactly what it is to be a 
data analyst. I have gone through all the phases of the project successfuly.
This project has been trully amazing and inpiring because it is very challenging. 
I have learned to use Python daily and all the routines to programatically
solve issues that manually would take countless hours. I have obtained professional
knowledge on how gather all the information of a database and produce a meaningful
outcome from it, that can be used to fulfill the company's goals.
All these skills can be used on my new position at the company. I can use my
knowledge of building Python applications to develop tools that will solve problems
related to scalability and accomodating millions of users. Database skills acquired
will be used to help network tools to handle future loads and improve performance.



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
```
P(O) -> P(O) -> P(C) -> P(C)
```
	
On the first chocolate we have P(O) = 6/10, 2nd is 5/9. Then P(C) is 4/8=½
and then 3/7. The following table resumes the information:


| Ate    | Probability | O left | C left |
|--------|-------------|------------|-------------
| -      |      -      | 6          | 4	|
| O      | 6/10        | 5          | 4	|	
| O      | 5/9         | 4          | 4	|
| C      | 1/2         | 4          | 3	|
| C      | 3/7         | 4          | 2	|
 
All this probabilities are independent so we can 
just calculate the total as:

```
P(A) = 6/10 x 5/9 x ½ x 3/7 = 1/14 = 0.0714 or 7%
```

### Follow up question:

If you were given an identical box of chocolates and again eat four 
pieces in a row, what is the probability that exactly two contain 
coconut filling?

There are 6 different possible order of events that allow us to eat exactly 2
Coconut chocolates. These are:

```
C C O O
O C C O
O O C C
C O O C
C O C O
O C O C
```

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
Of course this uoutput is expected, each individual probability is the same as the one above. This is because these are independent events, so the order you eat the chocolates does not matter, as long as you eat 2 of the Coconut filling.

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

The solution bellow work as intended. It is somehow verbose but it accounts
for all possible cases presented. Since I am using dictionaries, it has
a constant look-up time. I only need to go through the array twice. Once
when I am building the dict and a second time choosing which element of 
the dict to return, if any. This means the complexity of my algorith is 
of O(2N). The complexity should be less than O(2N) because we can only 
have as many keys in the dict, as we have symbols. If we only consider 
the alphabet this would be 26 keys max. So on my second iteration thorough
the keys, it would be of very reduced complexity in time and space. A very
long string would cause some complexity in saving the large indexes and count.
I could have done this with nested for loops, but that would
mean complexity of O(N^2) which is much worst.

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

            for key,value in letter.items():
                if value[0] == 1:
                    return key
		
    else:
        return None


print(first_unique('aabbcdd123'))
print(first_unique('112233'))
print(first_unique('a'))
```
The output of it will be:

```
> python first_unique.py
c
a
None
```

### Question 5 - What are underfitting and overfitting

in the context of Machine Learning? How might you balance them?

Overfitting happens when a model learns the detail and noise in the 
training data to the extent that it negatively impacts the performance
of the model on new data. This means that the noise or random fluctuations
in the training data is picked up and learned as concepts by the model.
Underfitting refers to a model that can neither model the training data 
nor generalize to new data. An underfit machine learning model is not a
suitable model and will be obvious as it will have poor performance 
on the training data.
Ideally we will want a sweet spot between underfitting and overfitting.
So you want the machine to learn the traning set rather well, but not too
much that it will not be able to adapt to new sets positevely. 

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



```
Junior Python Developer

Are you an up and coming Python or Golang Developer?

Do you enjoy building complex algorithms and storing huge amounts of data? If so, please read on!

Based in the heart of Orange County, Irvine, just a few steps from all the action, next to great shopping and dining, We are a high growth Cloud Technology / Content Streaming and Distribution company that enables users to access content, data, and services in real-time!

We are currently seeking a talented junior - mid Software Engineer with strong Python skills who can help develop solutions for our cloud services to support our growth as we sign up new customers and add millions of users.
Top Reasons to Work with Us
1. Custom work set - build your dream computer, tools or hardware setup
2. Exceptional benefits and flexible paid time off
3. Opportunity to see your ideals turn into code
What You Will Be Doing
- Creating tools and solving challenges related to scaling and accommodating millions of users
- Developing network side tools to accommodate and handle load, improve performance
- Building cloud technologies and improving performance
What You Need for this Position
- Understanding of Python and good knowledge of various Python Libraries, API's and toolkits
- Must be able to work with adult content. You will have limited exposure
- 1+ years of professional experience
- Know how to scale.
- Working knowledge of SQL
What's In It for You
- Strong Base Salary ($80,000 - $110,000 DOE)
- 401k Matching and Bonus!
- Projected company growth of over 10 times in the next 2-3 Years
- A new product that is revolutionizing distribution of high-demand content
- Solve challenging problems for a platform that is already serving a growing user base.

```
A year from now I would like to be a Mid Senior Python Developer that builds his own tools
to develop big data analysis for large companies. I would like to be designing algorithms 
and prediction models. Eventually moving into Machine Learning and Deep Learning domains
using that knowledge to develop better methods to extract and analyse data. I want to be able
to build any sort of web app with a Python back-end. I would like to be a project manager
for some project within the company, where I would have a team to lead.

The work I am currently working on will serve as basis for the position I am applying for.
I have been working with Python for the last 2 years, creating tools to analyse millions of
observation points of data. Using these tools to nuild prediction models for future events
and increase company's profits. the tools I have created are ready to handle heavy loads and 
future expansion of users. They store data on the cloud and not locally, in case of a security
breach or other case of accident, information is not sunddenly lost.

I am defintely looking forward to turn my ideas into code and produce results with it. Further 
enrich my knowledge of Python and data analysis it is big plus with this position


