from models.importer import ROOT_DIR, logger, get_data_from_csv, get_date



if __name__ == '__main__':
    logger.info("Let us see how we can create multiple CSV files out of one (consider it) BIG CSV File.")
    df_student = get_data_from_csv()
    for (gender), group in df_student.groupby(['gender']):
        file_name = f'{gender}_{get_date()}.csv'
        group.to_csv(f"{ROOT_DIR}\\output_dir\\{file_name}", header=True, index=False, mode='w+')
        logger.info(f"CSV File generated for {gender}, File Location: \\output_dir\\{file_name}")
