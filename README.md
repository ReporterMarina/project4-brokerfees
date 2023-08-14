 <!-- GETTING STARTED -->
## About the Broker Fees project

<h1>What I aimed to accomplish:</h1>

<p>I wanted to see how often apartment listings say that a tenant has to pay a broker fee. I also wanted to learn how to use Selenium for browser automation, how to better use Python for web scraping and Huggingface for artificial intelligence and machine learning. </p>

<br>
<br>
<h1>Short description of your findings</h1>
<p> There's little publicly available data about the prevalance of broker fees. </p>
<p> I looked at roughly 450 listings that explicitly said whether or not a broker's fee was required. </p>
<p> Three out of every four listings required tenants to pay a broker fee to move in. </p>
<p> Often, the fee was a month's rent. </p>
<p> Brokers often argue that requiring landlords to instead pay broker fees will end up raising rents for everyone over time. Indeed, some apartment listings tout "no broker fee" as a way to entice tenants wary of upfront costs. Median rent was higher for one and two-bedroom apartments.</p>
<b> But I found it's necessarily an across-the-board correlation. Studio apartments without broker fees had a lower median rent.</p>

<br>
<br>
<h1>Summary of the data collection process, with links</h1>
<br>
<p> I used Python and <a href="https://www.selenium.dev/downloads/"> Selenium</a> to scrape listings from dozens of pages of a rental website. I filtered for the most recent 30 days and for the greater Boston Area, including Cambridge and Somerville.</p>
<p>I then used Selenium to go through each URL one-by-one to scrape rental cost, beds, bath and rental description data.</p>
<p>This process was incredibly labor intensive and required me doing 100 listings at a time to ensure I could keep scraping. </p>
<p>I did look at APIs that scrape apartment websites for free. But they would tap out at 700 listings and I wanted more. </p>
<p>I wound up with thousands of listings from several apartment websites. I was originally going to stick with one major website, but had trouble scraping the data I wanted. I also realized it was better to use another website where I could filter listings from the past 30 days, so I could focus on the highly competitive Sept. 1 move-in season.</p>

<br>
<br>
<h1>Overview of the data analysis process</h1>
<p>Then, I merged the output in Python and used my dataset to train Hugging Face to create a machine learning model to help me start categorizing listings that included broker fees and similar phrases like realty fees.</p>
<p> Hugging Face required a good amount of trial and error to come up with a successful training data set. I initially got a 25% accurate model with just 3 data rows, then I got a 50% accurate model with about 40 rows. But when I used 25 rows, I for some reason got a <a href="https://huggingface.co/ReporterMarina/autotrain-binary_brokers-81863141870"> 65% accurate model </a>that I ended up using to at least sort a bunch of listings that definitely had broker fees. I was curious about whether the model would pick up on things like variations of broker/brokerage/realty fees and language about "no broker fees required" vs. "broker fees required."
<p>I used R to go through the data, clean it, join data, and create customized data frames so I could create filters. I was tempted to simply use Pivot tables again, but used R to make replicable pivot tables that I could easily export.  
<p>I also used R to filter phrases that would indicate broker fees were in a listing and whether or not they were required. I fed some descriptions to ChatGPT and had it propose some phrases I didn't think of.
<p>At the end of the day, I ended up going through hundreds of listings myself to verify how many required broker fees or not. </p>

<br>
<br>
<h1>A section about what new skills, approaches, etc you used, or where you grew the most during the project</h1>
<p> I gained skills in web scraping with Python, browser automation in Selenium, approaching machine learning models with Hugging Face and using R to more quickly and efficiently analyze data.  </p>

<br>
<br>
<h1>A section about things you tried to do or wanted to do but did not have the skills/time (but if you have more time you might do)</h1>
<p> It took many hours to gain confidence and expertise with Selenium through trial and error. With more time, it'd be great to do statistical analysis of the listings to come up with a representative sample so I could look at pricing with more precision and nuance. I would love to also get better at training the machine learning models to help with analyzing large amounts of text. 
</p>


<p>Link to Github project: <a href="https://reportermarina.github.io/project4-brokerfees/">here</a></p>