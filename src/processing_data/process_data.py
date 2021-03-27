import pandas as pd
from src.utils.json_util import GetJsonFromFile
from src.utils.regex_utils_time import get_date_time, validate_trundate


class Process_data_frame():


    @classmethod
    def read_data(cls,file_path,json_path):
        try:
            df = pd.read_csv(file_path)
            from more_itertools import chunked
            CHUNK_SIZE = 50000

            index_chunks = chunked(df.index, CHUNK_SIZE)
            output_df = pd.DataFrame()
            for ii in index_chunks:
                df_1=df.iloc[ii].copy()
                for i in df_1.columns:
                    df_1[i] = df_1[i].apply(lambda row: get_date_time(row))

                    df_1[i] = df_1[i].apply(lambda row: validate_trundate(row))
                    # import pdb
                    # pdb.set_trace()
                output_df=output_df.append(df_1)
            configs = GetJsonFromFile(json_path)
            if output_df.shape[0]>0:
                output_df = cls.rename_column_names(output_df, configs)
            return  output_df
        except Exception as e:
            pass
            # print(e)


        return df

    @classmethod
    def rename_column_names(cls,dataframe,mappings):
        dataframe.rename(columns=mappings, inplace=True)
        return dataframe