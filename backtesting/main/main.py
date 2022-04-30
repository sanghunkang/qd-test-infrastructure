import os
import sys
import shutil
import subprocess

def alter_libraries(PATH_TO_LIBRARIES):
    if 'exchange_calendar_xkrx.py' in os.listdir(PATH_TO_LIBRARIES+'trading_calendars/') :
        os.remove(PATH_TO_LIBRARIES+'trading_calendars/exchange_calendar_xkrx.py')
    shutil.copy('../zipline_files_to_replace/exchange_calendar_xkrx.py',PATH_TO_LIBRARIES+'trading_calendars/exchange_calendar_xkrx.py')

    if 'extensions.py' in os.listdir(PATH_TO_LIBRARIES+'zipline/') :
        os.remove(PATH_TO_LIBRARIES+'zipline/extensions.py')
    shutil.copy('../zipline_files_to_replace/extensions.py',PATH_TO_LIBRARIES+'zipline/extensions.py')

    if 'run_algo.py' in os.listdir(PATH_TO_LIBRARIES+'zipline/utils/') :
        os.remove(PATH_TO_LIBRARIES+'zipline/utils/run_algo.py')
    shutil.copy('../zipline_files_to_replace/run_algo.py',PATH_TO_LIBRARIES+'zipline/utils/run_algo.py')

    if 'csvdir.py' in os.listdir(PATH_TO_LIBRARIES+'zipline/data/bundles/') :
        os.remove(PATH_TO_LIBRARIES+'zipline/data/bundles/csvdir.py')
    shutil.copy('../zipline_files_to_replace/csvdir.py',PATH_TO_LIBRARIES+'zipline/data/bundles/csvdir.py')
    print('libraries changed')

def ingest_price_data(PATH_TO_LIBRARIES, VIRTUAL_ENV_NAME):
    if VIRTUAL_ENV_NAME == '' :
        subprocess.call('python {}zipline/extensions.py; zipline ingest -b usa_daily_bundle'.format(PATH_TO_LIBRARIES), shell=True)
        print('bundling finished')
    else :
        subprocess.call('source conda activate {0}; python {1}zipline/extensions.py; zipline ingest -b usa_daily_bundle'.format(VIRTUAL_ENV_NAME, PATH_TO_LIBRARIES), shell=True)
        print('bundling finished')
    
if __name__ == '__main__':
    # 내 환경에서만 작동, 패쓰를 그냥 입력받을까 고민중 (윈도우, 맥 차이)
    PATH_TO_LIBRARIES = [path for path in sys.path if 'site-packages' in path][0] +'/'
    VIRTUAL_ENV_NAME = PATH_TO_LIBRARIES.split('/')[PATH_TO_LIBRARIES.split('/').index('envs') + 1]

    alter_libraries(PATH_TO_LIBRARIES)
    
    # ingest_price_data(PATH_TO_LIBRARIES, VIRTUAL_ENV_NAME)
    from test import test_run
    test_run().run()
    print("mission completed!")