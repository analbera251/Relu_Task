# Relu_Task
This is a web scraping task given by Relu Consultancy.

Source URL - https://www.dailymotion.com/tseries2

Problem Statement - You are tasked with scraping video URLs uploaded by the T-Series on the Dailymotion website. Extract the video IDs of the first 500 videos. Additionally, you must find and count the most frequently repeated character in the video IDs.

Hint: You can use selenium to solve the question.

Here is a step-by-step breakdown of the task:

-Scrape all video URLs uploaded by the T- Series on Dailymotion website by visiting the following direct URL: T-Series Dailymotion.

-Collect the first 500 video URLs.

-Perform a case-insensitive search to find and count the most frequently repeated character in the video URLs Video ID.

Where is Video ID:

You can find the Video ID by looking for the hash value that comes after "video/" in the URL.

To Print the most repeated character and its count.

As an example, consider the following two video URLs:

v1 = https://www.dailymotion.com/video/x3j6mwpmh

v2 = https://www.dailymotion.com/video/x34zk8amde

Video ID of v1 = x3j6mwpmh

Video ID of v2 = x34zk8amde

Count of characters in collective IDs

Character: x, Count: 2
Character: m, Count: 3 
Character: a, Count: 1 
Character: j, Count: 1 
Character: w, Count: 1 
Character: p, Count: 1 
Character: z, Count: 1 
Character: k, Count: 1
Character: h, Count: 1
Character: d, Count: 1
Character: e, Count: 1
For Example -

In the example, you can see above that ‘m’ is highly repeated, so in the output, it should be printed as follows:

print("m:3")
Here, 'm' represents the character, and '3' represents its count. In case if characters have same count, then take that character which appears first in alphabetic order, Let’s say if ‘a’ and ‘d’ have count 4, then take ‘a’ as it appears first in alphabetic order.
