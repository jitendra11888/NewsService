# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
from flask import Flask, jsonify, request

# app = FastAPI() 

app=Flask(__name__)   



@app.get("/news")
def get_news():
    response = {
        "status": "ok",
        "totalResults": 7584,
        "articles": [
            {
                "source": {
                    "id": "the-times-of-india",
                    "name": "The Times of India"
                },
                "author": "Divyadeep Singh",
                "title": "S&P 500, Dow Jones, NASDAQ futures record upward movement after Wall Street sees big slump due to AI stocks, including Nvidia and suspense over interest rate cuts; check key indices",
                "description": "US stock futures saw a slight change after Wall Street experienced a significant downturn. Major indices like the Dow Jones, S&P, and Nasdaq futures showed modest gains. This followed a sharp fall on Thursday, November 14, 2025, driven by concerns over inflat…",
                "url": "https://economictimes.indiatimes.com/news/international/us/sp-500-dow-jones-nasdaq-futures-record-upward-movement-after-wall-street-sees-big-slump-due-to-ai-stocks-including-nvidia-and-suspense-over-interest-rate-cuts-check-key-indices/articleshow/125314573.cms",
                "urlToImage": "https://img.etimg.com/thumb/msid-125314612,width-1200,height-630,imgsize-194528,overlay-economictimes/articleshow.jpg",
                "publishedAt": "2025-11-14T02:43:15Z",
                "content": "After Wall Street saw one of its worst days in recent times, Stock futures witnessed slight but positive movement, with futures tied to the Dow Jones Industrial Average rising 65 points, or 0.1%. Oth… [+2673 chars]"
            },
            {
                "source": {
                    "id": None,
                    "name": "Twistedsifter.com"
                },
                "author": "Jayne Elliott",
                "title": "Hybrid Driver Needs An Electric Vehicle Spot To Charge His Car, So He Calls A Yoga Studio And Lies That Another Vehicle Is Being Towed",
                "description": "It's not that hard to be considerate of others.",
                "url": "http://twistedsifter.com/2025/11/hybrid-driver-needs-an-electric-vehicle-spot-to-charge-his-car-so-he-calls-a-yoga-studio-and-lies-that-another-vehicle-is-being-towed/",
                "urlToImage": "https://twistedsifter.com/wp-content/uploads/2025/10/Twisted-Sifter-90.png",
                "publishedAt": "2025-11-14T01:55:47Z",
                "content": "Shutterstock/Reddit\r\nImagine driving a hybrid or an electric vehicle but living in an apartment building where you can’t install an electric vehicle charger.\r\nIf you relied on electric vehicle charge… [+3905 chars]"
            },
            {
                "source": {
                    "id": "the-times-of-india",
                    "name": "The Times of India"
                },
                "author": "Reuters",
                "title": "Wall Street sinks as investors fret about rate cuts",
                "description": "Wall Street experienced significant declines on Thursday, driven by steep losses in AI heavyweights like Nvidia. Investors scaled back expectations of interest rate cuts due to inflation concerns and differing views among central bankers on the U.S. economy's…",
                "url": "https://economictimes.indiatimes.com/markets/stocks/news/wall-street-sinks-as-investors-fret-about-rate-cuts/articleshow/125313895.cms",
                "urlToImage": "https://img.etimg.com/thumb/msid-125313908,width-1200,height-630,imgsize-177726,overlay-etmarkets/articleshow.jpg",
                "publishedAt": "2025-11-14T01:47:34Z",
                "content": "Wall Street tumbled on Thursday, with steep losses in Nvidia and other AI heavyweights, as investors scaled back expectations of interest rate cuts due to inflation worries and divisions among centra… [+3356 chars]"
            }
        ]
    }

    return jsonify(content=response)

if __name__ == "__main__":
    app.run()
