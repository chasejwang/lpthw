#### Weak 0 Assignment Journal: 

[TOC]



I'm a newcomer for computer programing. Learning python in Py103 open another door of viewing world for me.

This journal is mainly the description of the differences between Python2 and Python3.

Meanwhile, I explained the ways and resources, by which I nailed down the week 0 assignment. The structure of this journal has those sectors, including differences between python 2 and 3, research srouces, the difference(mainbody), difficulties when doing researching, and "questions?".

I won't keep this structure for following week assignment journals until I feel that there are more efficient ways of structuring to organize journals for "me" to recall the information.

##### Research Sources:

[Cheat Sheet:Writing Python 2-3 compatible code](http://python-future.org/compatible_idioms.html)

[The Python Tutorial](https://docs.python.org/3/tutorial/index.html)





##### Difference between python 2 and 3:

In this sectors, I will explain the difference between python 2 and 3 from both philosophical and functional prospectives. 

In term of philosophical prospective of the difference, Python3 attempts to achieve the higher level of easiness and consistence among python languages.

such as: 

some aspects of the core language, such as print and exec being statement, integer using floor divison, have been adjusted to be easier and consistent with the rest of language. 

In term of the functional prospectives of the differences bewteen python 2 and 3, python 3 have the better *unicode support* and *saner bytes/Unicode separation*. 

##### The difference in examples:

|             items              |                 Python 2                 |                 Python 3                 |
| :----------------------------: | :--------------------------------------: | :--------------------------------------: |
|             print              | print 'Hello, Steve' <br\>print ("Hello, steve") |          print ('Hello, Steve')          |
|             input              |        raw_input() <br\> input()         |                 input()                  |
|            integer             |                   long                   |                   int                    |
|         division(math)         |                 3/2 = 1                  |                 3/2 =1.5                 |
| Unicode (text) string literals | s1 = 'The Zen of Python'  <br\> s2 = u '我们都是祖国的喇叭花\n' | s1 = u 'The Zen of Python'  <br\> s2 = u '我们都是祖国的喇叭花\n' |
|      Byte-String literals      |      s='This must be a byte-string'      |     s= b'This must be a byte-string'     |
| Imports relative to a package  |            Import submodule2             |         from . import submodule2         |
|              exec              |              exec 'x = 10'               |              exec('x = 10')              |



##### Difficutlies when doing reseraching: 

My major difficulties involved with this class are lack of enough knowldge base to achive my expected quality of each assignment. It is great to have chances to learn from other studenets, like 大猫大神.

After reading huangdaomao.com, I realized that there are three ways of improving my efficiency when taking progress in Py103 classes: 

1. Learning Markdown, Being familiar with it.
2. Understanding Hexo, creating my blog using it, and trying to sychronize my blog with githut.
3. Creating a blog

Afte reading huangdamao.com, I knew that there was a way to automate synchronization between github and personal blog. However, Wangjunyu and Simpleomao answered me about what knowledge base the newcomer should have to make the synchronization possilbe, making me think that there is a long way to go ahead. It doesn't make me get cold feet about it. What I need to do is to face the difficulties with effective solutions in hand.



##### Questions?

where to obtain study guides for Hexo and Markdown? 





