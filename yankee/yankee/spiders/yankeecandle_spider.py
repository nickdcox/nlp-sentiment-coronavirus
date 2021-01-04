import scrapy

class YankeeSpider(scrapy.Spider):
    name = "yankeespider"
    baseURL = []
    baseURL.append("https://www.amazon.com/product-reviews/B0014SUGEW/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B0044R5L6S/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B07FD45KN8/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B075TJR2XK/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B001WMKT2O/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B071Y5RJM1/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B000W3T9GG/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B000ORX6WI/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B008P8YTU6/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    baseURL.append("https://www.amazon.com/product-reviews/B0014SUGEW/ref=cm_cr_arp_d_viewopt_srt?pageNumber=")
    
    start_urls = []
    
    # Create a list of URLs to be scraped, by appending a page number to the end of the base URL.
    for j in range(10):
        for i in range(1,550):
            start_urls.append(baseURL[j] + str(i))
        
    def parse(self, response):
        for row in response.css('div.review'):
            
            item = {}
            
            item['Title'] = row.xpath('.//a[@data-hook="review-title"]/span/text()').extract()

            item['Author'] = row.css('span.a-profile-name::text').extract()
                        
            item['Date'] = row.css('span.review-date::text').extract_first()
            
            item['Rating'] = int(float(row.css('i.review-rating > span::text').extract_first().strip().split(' ')[0].strip().replace(',', '.')))

            item['Product'] = row.xpath('.//a[@data-hook="format-strip"]//text()').extract()
            
            item['Helpfulness'] = row.css('span.cr-vote-text::text').extract_first()
                 
            # Remove leading and trailing spaces from review.
            trans_table = {ord(c): None for c in u'\r\n\t'}
            item['Content'] = ' '.join(s.translate(trans_table) for s in row.xpath('.//span[@data-hook="review-body"]//text()').extract()).lstrip()

            yield item