#Installation Guides

##Install and Activate Python Virtual Environment
    '''  virtualenv venv-scrapy '''
    ''' source venv-scrapy/bin/activate ''' 

##Install Required Packages 
pip install -r requirements.txt

##Run the Project
Once the required python modules are installed you should be able to view/run the Python Scrapy Spider with the following command (from within the project folder):

Cd into the project spiders: '''cd Bookscraper/Bookscraper'''

View the project spiders: '''scrapy list '''

Run the project spider: '''scrapy crawl bookspider'''