import asyncio
import json
import websockets


async def main():
    url = ('wss://testnet.binancefuture.com/stream?'
           'streams=xrpusdt@kline_1h')
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']
            close_price = float(data['k']['c'])
            high_price = float(data['k']['h'])
            if close_price < high_price:
                one_percent = high_price / 100
                price_difference = high_price - close_price
                if price_difference >= one_percent:
                    print("Цена снизилась!!!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
