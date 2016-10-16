import os
from datetime import datetime
from io import BytesIO
from googleapiclient.discovery import build
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from djog.config.config import (UPLOAD_IMAGE, IMG_WIDTH_REQUIR, IMG_HEIGHT_REQUIR,
                                WATERMARK, WATERMARK_OPACITY)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_django.settings")
from djog.models.model_dogs import Breeds
from djog.servises.img_resizer_and_watermark_add import img_resizer_and_watermark_add

API_KEY = 'AIzaSyAENBpRgjuR8YRsVL09l-n41I_RHqwNfTs'
CUSTOM_SEARCH_ENGINE_ID = '017619512220957009035:2tzs1jfauia'
NUMBER_IMG_REQUIR = 2

def request_to_google_cse(api_key, query, custom_search_engine_id, number_img_requir):
    """
    Make a request to google custom search API.
    Google API Client Library for Python is used.
    :param api_key: the key query parameter to identify your application.
    :param query: query parameter to specify your search expression.
    :param custom_search_engine_id: specify the custom search engine you want to use to perform
    this search. (used 'cx' for a search engine created with the Control Panel)
    :param number_img_requir: required number of links that you need
    :return: data in JSON format. To access each link use: links['items'][i]['link']
    """
    service = build("customsearch", "v1",
                developerKey=api_key)
    links = service.cse().list(
        q=query,
        cx=custom_search_engine_id,
        fileType='jpg,png',
        imgSize='xxlarge',
        num=number_img_requir,
        searchType='image',
        fields='items/link'
        ).execute()
    return links


def download_images_by_link(number_img_required, links, image_width_requir, img_height_requir,
                            watermark, watermark_opacity, path_to_img_save):
    """
    Download images using links. Rename it, resize and put watermark.
    :param number_img_required: amount of images you want to download
    :param links: data in JSON format
    :param image_width_requir: required width of image
    :param img_height_requir: tequired height of image
    :param watermark: absolute path to watermark picture
    :param watermark_opacity: required watermark opacity
    :param path_to_img_save: absolute path to place for saving image
    """
    # use header because some links raise 403 error
    hdr = {'User-Agent': 'Mozilla/5.0'}

    for i in range(0, number_img_required):
        try:
            req = Request(links['items'][i]['link'], headers=hdr)
            image_on_web = urlopen(req)
            image_buffer = image_on_web.read()
            #  load raw data into a BytesIO container
            image_buffer_byte = BytesIO(image_buffer)
            image_buffer_edited = img_resizer_and_watermark_add(image_buffer_byte, image_width_requir,
                                                                img_height_requir, watermark,
                                                                watermark_opacity)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            new_img_filename = 'img_' + str(i) + '_' + timestamp + '.png'
            image_buffer_edited.save(os.path.join(path_to_img_save, new_img_filename), 'PNG')
            image_on_web.close()
            print(new_img_filename + ' was succesfully downloaded ')
        except HTTPError:
            print('HTTP Error 403: Forbidden. Link is not valid')


def main():
    if not os.path.exists(UPLOAD_IMAGE):
        os.makedirs(UPLOAD_IMAGE)

    breeds_list = Breeds.objects.all()
    for breed in breeds_list:
        print('Start downloading images for ' + str(breed))
        links = request_to_google_cse(API_KEY, breed, CUSTOM_SEARCH_ENGINE_ID, NUMBER_IMG_REQUIR)
        folder_single_breed_img = os.path.join(UPLOAD_IMAGE, str(breed))
        # create folder for each breed if it isn't exist
        if not os.path.exists(folder_single_breed_img):
            os.makedirs(folder_single_breed_img)
        download_images_by_link(NUMBER_IMG_REQUIR, links, IMG_WIDTH_REQUIR, IMG_HEIGHT_REQUIR,
                                WATERMARK, WATERMARK_OPACITY, folder_single_breed_img )


if __name__ == '__main__':
     main()
