# URLs
VEGETABLES_URL_LIDL = 'https://sortiment.lidl.ch/de/obst-gemuse/gemuse.html#/'

# --------------------------------------
# XPaths

# Buttons
REJECT_COOKIES_BUTTON_XPATH = '//button[@id="onetrust-reject-all-handler"]'
LOAD_MORE_BUTTON_LIDL_XPATH = '//button[@class="primary amscroll-load-button-new"]'

# Items List
LIST_ITEM_DETAILS_CONTAINER_XPATH = ('//li[@class="item product product-item"]/div[@class="product-item-info"]/div['
									 '@class="product details product-item-details"]')
LIST_ITEM_DETAILS_ITEM_LINK_XPATH = '//div[@class="product details product-item-details"]/a[@class="product-item-link"]'
LIST_ITEM_DETAILS_ITEM_NAME_XPATH = '//strong[@class="product name product-item-name"]'
LIST_ITEM_DETAILS_ITEM_ORIGIN_XPATH = '//div[@class="product description product-item-description"]'
LIST_ITEM_DETAILS_ITEM_PRICE_XPATH = '//div[@class="price-box price-final_price"]//strong[@class="pricefield__price"]'
LIST_ITEM_DETAILS_ITEM_PRICE_PER_XPATH = ('//div[@class="price-box price-final_price"]//span['
										  '@class="pricefield__footer"]')
LIST_ITEM_DETAILS_ITEM_QUANTITY_XPATH = '//div[@class="price-box price-final_price"]//span[@class="pricefield__footer"]'
