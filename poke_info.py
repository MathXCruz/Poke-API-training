import logging
import traceback
from poke_api.extract import get_info
from poke_api.transform import summarize


def main():
    logging.info('poke_info(poke_api) : start running')
    poke_name_id = input('Enter a pokemon name or id: ').lower()
    try:
        pokemon = get_info('pokemon', poke_name_id)
        print(summarize(pokemon))
    except Exception as not_found:
        print(
            'Sorry, pokemon not found. Please check the spelling \
and try again.'
        )
        logging.critical(f'main(poke_api): unexpected error - {not_found}')
    logging.info('poke_info(poke_api) : end running')


if __name__ == '__main__':
    logging.root = logging.getLogger('user')
    logging.basicConfig(
        level=logging.INFO,
        filename='logs.log',
        format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filemode='a',
    )
    try:
        main()
    except Exception as e:
        tb = ''.join(traceback.format_tb(e.__traceback__))
        tb = tb.replace('\n', ' - ')
        logging.critical(f'poke_info(poke_api): unexpected error - {e} {tb}')
        raise e
