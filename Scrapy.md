# Web Scraping with Scrapy: A Quick Guide

This guide will walk you through the basic steps of web scraping with Scrapy, including how to handle pages that render dynamically using JavaScript. The resources provided will help you get started with Scrapy and teach you how to scrape dynamic content effectively.

For a brief comparison of other popular scraping tools like Beautiful Soup, Scrapy, and Selenium, check out this video: [Beautiful Soup vs. Scrapy vs. Selenium](https://www.youtube.com/watch?v=-qRLWOtn_Kc).


## Getting Started with Scrapy

Before diving into dynamic content, it's essential to get familiar with Scrapy, a powerful and versatile web scraping framework. Begin by following the official Scrapy tutorial:

- **Scrapy Official Tutorial**: [Scrapy Documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)

## Handling Dynamic Pages

When dealing with dynamic content (content rendered using JavaScript), you'll need to take additional steps to ensure that you scrape all the data correctly.

### 1. Checking if a Page Renders Using JavaScript

Sometimes, pages load content dynamically using JavaScript. To determine if a page relies on JavaScript for rendering:

- **Disable JavaScript**: 
  1. Open the browser's Developer Tools (`Ctrl + Shift + I`).
  2. Press `Ctrl + Shift + P` and search for "Disable JavaScript."
  3. Reload the page and check if the content is still visible.

- **Enable Caching**:
  1. In the Developer Tools, go to the "Network" tab.
  2. Press `Ctrl + Shift + P` and search for "Enable JavaScript."

For a visual explanation, watch this video:
- **Video Tutorial**: [How to Check if a Page Renders Using JavaScript](https://www.youtube.com/watch?v=Pu3gmdWsLYc)

### 2. Inspecting Network Requests for JSON Data

Dynamic pages often load content via XML or JSON requests. You can inspect these requests in the Developer Tools:

- **Check for XML/JSON Requests**:
  - In the "Network" tab of the Developer Tools, look for any XML or JSON requests.
  - Preview the JSON data to see if it contains the content you want to scrape.

### 3. Scraping Dynamic Content with Scrapy + Splash

For pages that rely heavily on JavaScript, you can use **Scrapy + Splash** to scrape content. Splash is a headless browser designed to render pages and execute JavaScript, making it easier to scrape dynamic websites.

- **Splash Setup**: 
  - Splash can be run in a Docker container. Ensure you have Docker installed, then pull the Splash image: `docker pull scrapinghub/splash`.

- **Scrapy + Splash Tutorial**:
  - Follow this video to learn how to set up and use Scrapy with Splash: [Scraping Dynamic Pages with Scrapy + Splash](https://www.youtube.com/watch?v=RgdaP54RvUM)

## Conclusion

By following these steps and using the provided resources, you'll be well-equipped to scrape both static and dynamic web pages using Scrapy. Remember that practice is key, so experiment with different websites to hone your skills.

Happy scraping!
