import yaml
from nltk.corpus import stopwords

config_dict = dict()

config_dict['PATTERN'] = {'NAME': [{"POS": "PROPN"}, {"POS": "PROPN"}],
                          'EDUCATION': [ 'BE','B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E', 'M.E.', 'MS', 'M.S', 'BTECH', 'MTECH', 'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'],
                          'NOT_ALPHA_NUMERIC': r'[^a-zA-Z\d]','NUMBER': r'\d+'}

config_dict['DATES'] = {'MONTHS_SHORT':r'(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)',
                        'MONTHS_LONG':r'(january)|(february)|(march)|(april)|(may)|(june)|(july)|(august)|(september)|(october)|(november)|(december)',
                        'MONTHS':r'(((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec))((ruary)|(ch)|(il)|(e)|(y)|(e)|(y)|(ust)|(tember)|(ober)|(ember))?)',
                        'YEAR':r'(((20|19)(\d{2})))'}

config_dict['NLP'] = {'STOPWORDS': set(stopwords.words('english')),
                      'RESUME_SECTIONS' : ['accomplishments','experience','education','interests','projects','professional experience','publications','skills']}

config_dict['TEST'] = {'text': 'Kaushik Ilango Jersey City, NJ | P: +1 5513706260 | kilango5@outlook.com | GitHub | LinkedIn EDUCATION Stevens Institute of Technology Hoboken, NJ Master of Science in Computer Science Expected Dec 2023 Graduate Certificate in Machine Learning Expected Dec 2023 National Institute of Technology Karnataka Surathkal, KA Bachelor of Technology in Computer Science and Engineering Jul 2016 - Jul 2020 SKILLS Technical Languages: Python, C, C++, SQL, Oracle, MongoDB, MATLAB Frameworks: NumPy, Pandas, Scikit, NLTK, TensorFlow, Keras, Django, LAMP, AWS, PyTorch, TensorFlow Tools: Docker, GitHub, PostgreSQL, MySQL, Oracle, Kubernetes, Data Visualization Platforms: Linux, Web, Windows, GCP WORK EXPERIENCE Software Development Engineer II Hyderabad, TL Head Digital Works Jun 2020 – Jul 2022 ● Implemented game features and models, improving user game experience and involvement by 65% on proprietary platform. Aggregated unstructured data from 20+ sources to build the foundation of a new product; led to $100,000 in new revenue'}

with open('config.yaml','w') as yamlfile:
    yaml.dump(config_dict,yamlfile)

