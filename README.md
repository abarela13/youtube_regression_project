# Project 2: Regression - YouTube Growth Predictor
## Identifying what affects channel viewership for small channels
## Abstract
The goal of this project was to use regression models to predict the total channel viewership of fairly "new" youtube channels (less than 2 year) in order to project possible revenue for channels with monetization. I worked with data scraped from [ChannelCrawler](https://channelcrawler.com) and [SocialBlade](https://socialblade.com/).
### Data
The dataset ultimately contains 854 observations with 8 features for each.
 * **acquisition**: web scraping
 * **storage**: flat files
 * **sources**:
    - [ChannelCrawler](https://channelcrawler.com)
    - [SocialBlade](https://socialblade.com/)
### Target variable:
 - Total Channel Views
### Features:
  - Videos Published
  - Channel Creation Date (Age)
  - Channel Views
    - Total
    - Weekly
  - Subscribers
   - Total
   - Weekly Gained/Lost
 - Monetized
### Algorithms:
 - Simple Linear Regression
 - Ridge Regression
 - Lasso Regression
### Tools:
 - Web Scraping
    - `BeautifulSoup`, `Selenium`
 - Data Cleanup
    - `Pandas`
 - Modeling
    - `scikit-learn`, `statsmodels`
### Analysis:
 * Model: Linear Regression
 * Feature engineering: `StandardScaler`,`PolynomialFeatures`
 * Cross-Validation
 * Regularization: `Ridge`, `Lasso`, `RidgeCV`, `LassoCV`