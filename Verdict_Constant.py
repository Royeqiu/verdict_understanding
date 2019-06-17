class Verdict_Constant:
    title = 'jtitle'
    full_text = 'jfull'
    main_content = ['主 文','主文']

    people_name = '被移送人'
    newline = '\r\n'
    period = '。'
    duplicate_space = '  '
    single_space = ' '

class Unsafe_Driving_Constant(Verdict_Constant):

    type_one_keyword = '酒精濃度'
    type_two_keyword = ''
    type_three_keyword = ''
    confirm_keyword = '不能安全駕駛'

verdict_constant = Verdict_Constant()
unsafe_driving_constant = Unsafe_Driving_Constant()
