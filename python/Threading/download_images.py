import os
import requests
import time
import threading
import multiprocessing
import asyncio
import aiohttp
from urllib.parse import urlsplit
import sys
import argparse

def download_image(url):
    start_time = time.time()
    response = requests.get(url)
    response.raise_for_status()
    
    url_path = urlsplit(url).path
    filename = os.path.basename(url_path)
    
    with open(filename, 'wb') as file:
        file.write(response.content)
    
    end_time = time.time()
    print(f"Downloaded {filename} in {end_time - start_time:.2f} seconds")

def download_images_multithreaded(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def download_images_multiprocessing(urls):
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

async def download_image_async(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        response.raise_for_status()
        content = await response.read()
    
    url_path = urlsplit(url).path
    filename = os.path.basename(url_path)
    
    with open(filename, 'wb') as file:
        file.write(content)
    
    end_time = time.time()
    print(f"Downloaded {filename} in {end_time - start_time:.2f} seconds")

async def download_images_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, url) for url in urls]
        await asyncio.gather(*tasks)

def main():
    parser = argparse.ArgumentParser(description="Download images from URLs using different approaches.")
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='URLs of images to download')
    parser.add_argument('--method', choices=['threading', 'multiprocessing', 'asyncio'], default='threading',
                        help='Method to use for downloading images')
    
    args = parser.parse_args()
    urls = args.urls
    method = args.method
    
    start_time = time.time()
    
    if method == 'threading':
        download_images_multithreaded(urls)
    elif method == 'multiprocessing':
        download_images_multiprocessing(urls)
    elif method == 'asyncio':
        asyncio.run(download_images_async(urls))
    
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()
