from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import yaml
import re
def extract_experience(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words and wordnet_lemmatizer.lemmatize(w) not in stop_words] 
    sent = nltk.pos_tag(filtered_sentence)
    
    cp = nltk.RegexpParser('P: {<NNP|NN>+}')

    cs = cp.parse(sent)

    experiences = []
    print(experiences)
    for vp in list(cs.subtrees(filter=lambda x: x.label()=='P')):
        experience_text = " ".join([i[0] for i in vp.leaves() if i[1] in ['NNP', 'NN']])
        experiences.append(experience_text)

    return experiences

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

text = config['TEST']['text']


resume_text = """John Smith
123 Main Street, Anytown, USA 12345
Phone: 555-1234 | Email: johnsmith@email.com

PROFESSIONAL SUMMARY
Dynamic and motivated marketing professional with 5+ years of experience driving growth and engagement through data-driven content strategies and innovative campaign development. Skilled at building cross-functional partnerships and tailoring messaging to resonate with diverse audiences across digital and print channels.

CORE SKILLS AND EXPERTISE  
- Content Creation: Copywriting, graphic design, video production
- Campaign Management: Budgeting, performance analysis, reporting  
- Data Analytics: A/B testing, audience segmentation, campaign optimization
- Partnership Building: Influencer outreach, brand collaborations, ambassador programs

PROFESSIONAL EXPERIENCE
Content Marketing Manager, XYZ Inc. | Aug 2019 – Present
- Increased website traffic 32% YoY by optimizing content for SEO and implementing metadata best practices.  
- Improved email campaign ROI by 15% and grow subscriber base by 250% using sentiment analysis to refine messaging and cadence.
- Partnered with over 100 influencers across multiple verticals to create and distribute co-branded assets driving over 5M impressions.

Digital Marketing Coordinator, 123 Industries | Jan 2017 – Aug 2019  
- Planned and executed all web, SEO/SEM, email, social media and display advertising campaigns.
- Managed campaign budgets totaling over $2MM and made data-driven optimization decisions to control CPAs. 
- Developed and presented quarterly performance reports to executives leading to a 20% budget increase for high-performing channels.  

EDUCATION  
University of Michigan, Bachelor of Business Administration in Marketing, May 2015 – Apr 2017"""

print(extract_experience(resume_text))