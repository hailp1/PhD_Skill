# BẢN PHÂN TÍCH TOÀN VĂN: 2022_WANG_HOW_LIVE_STREAMING_CHANGES_SHOPPING_DECISIONS_IN_E-COMMERCE_
- **Nguồn tệp gốc:** `2022_Wang_How_Live_Streaming_Changes_Shopping_Decisions_in_E-commerce_.pdf`
- **Thời gian nạp:** 27/11/2026 19:24:47
- **Tổng số trang:** 29 trang

---

## TRANG 1

(
:
–
701 729
2022) 31
Vol.:(0123456789)
Computer Supported Cooperative Work (CSCW)
https://doi.org/10.1007/s10606-022-09439-2
How Live Streaming Changes Shopping Decisions 
in E‑commerce: A Study of Live Streaming 
Commerce
Ye Wang*1, Zhicong Lu2, Peng Cao3, Jingyi Chu4, Haonan Wang5 & 
Roger Wattenhofer1
*1 ETH Zurich, Zurich, Switzerland (E-mail: wangye@ethz.ch; E-mail: wattenhofer@
ethz.ch); 2 City University of  Hong Kong, Kowloon  Tong, Hong  Kong (E-mail: zhiconlu@
cityu.edu.hk); 3 Massachusetts Institute of Technology, Cambridge, MA, USA (E-mail: pengcao@
mit.edu); 4 The University of Edinburgh, Edinburgh, UK (E-mail: s2071279@ed.ac.uk); 5 Carnegie 
Mellon University, Pittsburgh, PA, USA (E-mail: haonanw@andrew.cmu.edu)
Accepted: 17 June 2022
Abstract.  Live Streaming Commerce (LSC) is proliferating in China and gaining traction 
worldwide. LSC is an e-commerce service where sellers communicate with consumers through 
live streaming while consumers can place orders within the same system. Despite the signifi-
cant involvement of consumers in LSC, it has not been systematically analyzed how consumers 
make shopping decisions when engaging with LSC. In this paper, we conduct a mixed-methods 
study, consisting of surveys (N1 = 240) and follow-up interviews (N2 = 16) with LSC consum-
ers. We focus on two features of LSC, i.e., the communication between merchants and con-
sumers through live streaming and the participation of streamers, and aim to understand how 
these changes influence consumers’ decision-making process in LSC. We find that LSC enables 
merchants to exchange information with consumers based on their needs and provide additional 
customer services. Because of the appropriate information about the products they acquire and 
the enjoyable shopping atmosphere, consumers are willing to purchase products in LSC. As the 
intermediaries between merchants and consumers, streamers utilize their independent identity 
from merchants to enhance consumers’ awareness of shopping and persuade their online shop-
ping decisions. Moreover, we consider the opportunities and challenges of current LSC services 
and provide implications for LSC services and the research community regarding the develop-
ment of LSC.
Keywords:  E-commerce, Live streaming, Consumer decision-making process, Decision support 
systems
© The Author(s), 2022
ECSCW CONTRIBUTION

## TRANG 2

Y. Wang et al.
1  Introduction
“All girls, get ready, buy it!” At midnight of February 24, 2020, when Li Jiaqi 
just stopped speaking, 20 million consumers, who were watching his live stream, 
snapped up 80,000 eye shadows within one second1. The success indicates that 
live streaming marrying e-commerce (together: Live Streaming Commerce, LSC) 
may be the future of e-commerce. A statistic from China Internet Network Infor-
mation Center shows that, by January 2021, 32.9% of Chinese Internet users, 309 
million people, had participated in LSC (CINIC, 2020). LSC has also been gain-
ing worldwide traction. Walmart, for example, has expressed interest in utilizing 
TikTok’s LSC services in the United States (Zhong, 2020).
As shown in Figure 1, LSC provides a novel online shopping experience to 
consumers than traditional e-commerce services and enables a novel com-
munication channel between sellers and consumers. Consumers receive real-
time information and watch live streaming performances of streamers during 
the entire consumer decision-making process (Erasmus et  al., 2001). Given 
that human–computer interaction (HCI) and computer supported cooperative 
work (CSCW) researchers (Moser et al., 2017, 2019) have explored the severe 
impact of the system design and e-commerce model on consumers’ decisions in 
traditional online shopping, we aim to explore factors that determine the shop-
ping decision of consumers in LSC. By studying the decision-making process 
in LSC, we can better identify the challenges and opportunities in current LSC 
systems, which may inspire the future design of systems to support consumers’ 
online shopping experiences. In particular, we examine the factors of LSC which 
influence the decision-making process from two perspectives: first, the technol-
ogy perspective, i.e., how does live streaming technology influence the purchase 
decision making in LSC. And second, the human perspective, i.e., how do live 
streaming interactions between sellers and buyers influence the purchase decision 
making in LSC.
Compared to traditional e-commerce services, where consumers complete the 
online shopping process on the website, LSC enables merchants and consum-
ers to exchange information in real-time and affords one-to-many communication 
(Hamilton et al., 2014). Furthermore, entertaining live streaming elements have 
also been introduced into LSC (Li et al., 2019; Lu et al., 2018), which afford 
user engagement, and further influence the decision-making process of users in 
LSC. In other words, LSC serves as a decision support system in the consumer 
decision-making process. To better understand how live streaming influences 
consumer making decisions in LSC, we aim to address the following research 
question:
1  The video record of the live stream: https://​www.​bilib​ili.​com/​video/​av914​90264/
702

## TRANG 3

How Live Streaming Changes Shopping Decisions in E‑commerce:…
Figure 1.   The interface of Taobao Live. a) When users browse products on e-commerce platforms, they can notice whether the product is on sale 
in LSC and can directly enter the live streams by clicking the icon. b) Users can view all products on sale in LSC when they watch the live streams. 
They can send messages to streamers. c) Users can enter the website of the products without leaving the live streams. d) Users can place the order while 
the live stream thumbnail is placed at the left bottom corner of the website. e) The live stream image keeps in the interface during the entire process of 
online shopping
703

## TRANG 4

Y. Wang et al.
RQ1	
How do users perceive the affordances and the challenges of live streaming in the 
decision-making process in LSC?
On top of providing communication channels between merchants and consum-
ers during online shopping process, LSC also introduces market intermediaries 
(Chen et al., 2020), i.e., streamers, into LSC. LSC streamers can collaborate 
with different merchants and sell products provided by them. Therefore, LSC 
streamers serve as a third party between consumers and merchants in LSC. By 
introducing third party participants to online shopping, it is not clear how mar-
ket intermediaries influence the behavior of consumers in LSC. Therefore, we 
ask the following research question:
RQ2	
How do users perceive the affordances and the challenges of streamers in the decision-
making process in LSC?
We conduct a mixed-methods study, which consists of an online survey (N = 
240) and interviews (N = 16) with LSC consumers to investigate the affor-
dances and challenges consumers perceive in the decision-making process 
in LSC. We find that the perceived usability and usefulness of the products 
consumers were interested in, was positively influenced by the information 
provided via live streaming. Streamers also provide additional customer ser-
vices to create an enjoyable shopping environment during the period of online 
shopping and enhance consumers’ recognition of the online stores. Moreover, 
streamers utilize live streaming entertaining features to enhance consumers’ 
pleasure and arousal, and thus incentivize consumer shopping intentions in the 
decision-making process. However, since all consumers in LSC share the same 
communication channel with streamers, some experienced consumers perceive 
the information in LSC as repetitive, and the shopping efficiency decreases 
as they become familiar with LSC. Because of the perceived independence 
between LSC streamers and merchants and the recognition of streamers in 
other live streaming practices, consumers have been influenced by streamers 
in their decision-making process, especially in the stages of shopping need 
awareness, purchase decision and post-purchasing evaluations. On the other 
hand, streamers control the source of information consumers get in LSC, 
and their dominance has been perceived as a challenge by consumers in LSC 
practices.
This paper makes three contributions by understanding the emerging socio-
technological phenomenon. First, we study the consumer decision making 
process in LSC, and consider the influence of live streaming and the market 
intermediary participant. Second, we analyze the affordance of live streaming 
in e-commerce practices and explore how live streaming elements can influ-
ence non-live streaming practices. Finally, we provide design implications on 
how to break through the limitations of the current LSC.
704

## TRANG 5

How Live Streaming Changes Shopping Decisions in E‑commerce:…
2  Background and Related Work
The story of LSC starts from shopping guide websites. When making an online 
shopping decision, consumers would like to take opinions from others as a ref-
erence, which is called electronic word-of-mouth (eWOM) (Dellarocas,  2003; 
Hennig-Thurau et al., 2004). Sevitt and Samuel (2013) showed that more than 
72% of shoppers paid attention to recommendations when browsing Pinterest. In 
China, consumers are also interested in other people’s comments on products and 
several community-based online review websites, e.g., MOGU, have been devel-
oped for more than ten years (Peng et al., 2016). Shopping guide websites enable 
users to share their online shopping experiences, comments on products and rec-
ommend products with a link to the online shopping website. They will be paid 
commission if other consumers purchase products from the link.
Another similar phenomenon as LSC is TV shopping (Darian, 1987), which 
has substantially grown since the 1980s (Stephens et al., 1996). Hosts present a 
live show to demonstrate and introduce products, and respond to consumers ques-
tions from telephone inquiries (Stephens et al., 1996). Programs on TV shopping 
focus on promoting and selling products to obtain profits, which suggests that TV 
shopping channels are business channels but not entertaining television programs 
(Engel et al., 2000). Shopping convenience (Lim and Kim, 2011), satisfaction of 
entertainment requirements (Cortese and Rubin, 2010), reduction of loneliness 
(Kang and Ridgway, 1996), and the “parasocial interaction” between consumers 
and hosts (Park and Lennon, 2004; Alperstein, 1991) have been considered as 
the main motivations of consumers to participate in TV shopping. In China, the 
market size of the TV shopping peaked in 2015, with 39.9 billion CNY (MOF-
COM, 2018). The poor communication between consumers and merchants, the 
lower price advantage of products, the high production costs of TV shopping 
programs, and the development of online shopping, have impeded the develop-
ment of TV shopping channels in China (Li 2020; Liu, 2021).
With the development of 4G and the declining cost of mobile traffic in China, 
there was a spurt in live streaming, enabling more efficient real-time commu-
nication between individuals. Live streaming has become one of the most pop-
ular entertaining internet applications in China. By June 2020, live streaming 
attracts 562 million users, accounting for 59.8% of all Chinese internet users 
(CINIC,  2020). Therefore, shopping guide websites introduce the live stream-
ing service, which enables users to present products beyond texts and images. 
Because shopping guide websites strongly influence people’s shopping decision 
(Peng et al., 2016) and earn more than 6,000 million RMB of commissions from 
e-commerce platforms per year, e-commerce platforms terminated cooperation 
with shopping guide websites. Afterward, e-commerce platforms, such as Tao-
bao, developed their own LSC services and shopping guide websites began to 
transform into e-commerce platforms. Meanwhile, video/streaming platforms 
also encourage the streamers to conduct e-commerce practices and build internal 
705

## TRANG 6

Y. Wang et al.
online shopping systems (Day, 2022). Nowadays, e-commerce live streaming has 
become the most popular type of live streaming and attracts 32.9% of all Chinese 
internet users.
In the following, we review the most related work in three aspects: decision-
making in online shopping scenarios, market intermediaries in e-commerce, and 
live streaming affordances.
2.1  Consumer Decision Making in Online Shopping
A purchase decision is a behavior of consumers to determine and follow a deci-
sion-making process to reach a choice of purchase (Erasmus et al., 2001; Howard 
and Sheth, 2001). Holtzman (1988) describes the process of decision-making in 
three stages: formulation, evaluation and appraisal. In the context of online shop-
ping, several models (Hawkins et al., 2009; Howard and Sheth, 2001; Nicosia 
and Mayer 1976) capture the consumer buying behavior, and classify user behav-
ior in five fundamental stages: shopping need awareness, information search, 
alternative evaluations, deciding to purchase, and post-purchasing evaluation.
When making the online shopping decisions, consumers have to consider two 
perspectives: what to buy and where to buy (Koo et al., 2008). In other words, 
consumers will evaluate both, products and online stores during the decision-
making process (Jarvenpaa et al., 2000), including perceived usefulness and per-
ceived ease-of-use of products and their trusts of the online store (Van der Hei-
jden et al., 2003). Communication between sellers and consumers is crucial for 
such evaluations (Thomas, 2005). More than 50% of consumers expect advice 
from sellers about products they are interested in (Keeling et al., 2010) or per-
sonalized recommendations on their purchase (Agnihotri et al., 2009). Moreo-
ver, the diversity of information (Lowry et al., 2015) and real-time communica-
tions (Keeling et al., 2010) are preferred by consumers in their shopping decision 
making processes. On the other hand, consumers’ emotions, such as pleasure, 
arousal, and dominance (Mehrabian and Russell 1974), also have significant 
impacts on their shopping behaviors (Gorn et al., 2001; Szymkowiak et al., 2021; 
Coker, 2020), and further determine their online shopping decisions (Hagtvedt 
and Patrick 2008; Herabadi et al., 2009).
To help consumers to conduct online shopping decisions, decision support 
systems have been introduced to e-commerce systems (Kasper,  1996), includ-
ing interactive decision aids (Häubl and Trifts, 2000) and decision support tech-
nologies (Wang and Benbasat, 2008). Previous studies focus on decision support 
systems interacting with consumers, such as recommendation agents that assist 
consumers to screen products (Lin et al., 2010), comparison matrix that help con-
sumers to organize product information (Alba et al., 1997) and virtual reality and 
augmented reality that provide immersive shopping environments (Peukert et al., 
2019).
706

## TRANG 7

How Live Streaming Changes Shopping Decisions in E‑commerce:…
LSC introduces a novel decision support system into e-commerce, which sup-
ports real-time communication between sellers and consumers, i.e., live stream-
ing (Cai et al., 2018; Cai and Wohn, 2019). Cai et al. (2018) conducted a sur-
vey study among English-speaking participants to investigate the motivations 
of consumers to watch live streams, such as Amazon style live code, Facebook 
Live, and YouTube Live, when they search information of products. They sum-
marized that product demonstrations and product information are the main utili-
tarian motivations, while the interaction between consumers and streamers is the 
main hedonic motivation to watch a live stream of e-commerce. Later on, they 
elaborated their survey results with a gratification framework and identified four 
motivations, i.e., enjoyment of interaction, substitutability of personal examina-
tion, need for community and trend setting (Cai and Wohn, 2019). However, it is 
not clear how live streaming influences consumers’ shopping decisions in LSC, 
from both positive and negative perspectives, for instance, the efficiency of infor-
mation delivery (Lowry et al., 2015), the stimulation of impulse buying (Moser 
et al., 2019), and personalized recommendations (Agnihotri et al., 2009). To fill 
this research gap, we aim to understand how live streaming in LSC can influence 
the evaluations of products and online stores in this paper.
2.2  Intermediaries in E‑commerce
Market intermediaries are usually referred to the agents who establish and main-
tain market relationships between merchants and consumers (Chen et al., 2020). 
On the one hand, market intermediaries help merchants to find proper pools of 
buyers (Pazgal and Soberman, 2008). On the other hand, market intermediar-
ies can help consumers in searching, evaluating, and comparing products (Chen 
et al., 2002). E-commerce platforms are considered as the most common market 
intermediaries in e-commerce (Chakravarty et al., 2014).
Recently, more and more market intermediaries have been introduced in 
online shopping practices. Previous studies have examined two types of mar-
ket intermediaries in e-commerce: internet influencers (Geng et  al., 2020) 
and average people (Chen et al., 2020; Cao et al., 2020, 2021). Internet influ-
encers can earn fortunes with their fame by acting as market intermediar-
ies between merchants and their fans (Ku et  al., 2019). The existing cred-
ibility between them and their fans can positively influence the shopping 
decisions made by the targeted consumers. Moreover, the sense of fan com-
munity reinforces consumers’ purchase intention (Geng et  al., 2020). Cao 
et al. (2021,2020) and Chen et al., (2020) have studied market intermediaries 
who are average people. These intermediaries recommend and sell products 
to their friends, relatives and other people in their social network through 
social media. They serve as either local trend detectors or socially-connected 
convenience stores to satisfy consumers who have close relationships with 
707

## TRANG 8

Y. Wang et al.
them (Chen et al., 2020). The peer-to-peer trust in existing social networks 
and the trust of the community encourage consumers to make shopping deci-
sions with these intermediaries (Cao et al., 2021).
Compared to market intermediaries studied in previous work, LSC 
streamers interact with their consumers directly through live streaming 
and they actively participate in every stage of the decision-making process 
of consumers in LSC. Therefore, in this paper, we aim to understand how 
streamers behave as market intermediaries to influence consumer decision-
making in LSC.
2.3  Live Streaming and Its Affordances
Live streaming enables people to share images and voices in real-time (Haim-
son and Tang, 2017). This technology brings increased interactivity between 
people who are not in the same location for many activities in daily life, 
including entertainment, education, and social activities (Lu et  al., 2018). 
Live streaming has been widely studied in the field of HCI and CSCW, of 
which contents including video games (Cheung and Huang, 2011; Li et  al., 
2018), online performance (Taber et  al., 2019), online education (Hew and 
Hara, 2007; Ma and Yuen, 2011), and social activities (Dougherty, 2011).
Affordances have been defined broadly in the field of HCI and CSCW. We 
root our work in Gibson (1977) and Hutchby (2001)’ s definitions, defined as 
the qualities, features, or cues within a technology that affords uses to indi-
viduals (Aakhus, 2007; Nagy and Neff, 2015; Postigo, 2016). Previous work 
have examined multiple affordances of live streaming, including real-time 
communication (Sjöblom and Hamari,  2017), multi-dimensional informa-
tion exchange (Taber et al., 2019), hot and cool media (McLuhan, 1994), and 
one-to-many communication (Hamilton et al., 2014). These affordances have 
constructed relaxing environments (Sjöblom and Hamari, 2017), connected 
audiences with like-minded people (Taber et al., 2019) and formed communi-
ties to extend the social relationships between participants (Lottridge et  al., 
2017). Moreover, since the majority of live streaming is entertaining, some 
features have been involved in live streaming systems as the affordances of 
entertainments (Lu et al., 2018), e.g., Danmuku (Ma and Cao, 2017), virtual 
gifts (Lu et al., 2018), platform-wide competitions (Cunningham et al., 2019), 
and “Lianmai”, which allows two streamers to have a video chat during their 
live streams (Li et al., 2019).
However, previous studies have not investigated the live streaming affordances 
of online shopping activities. As e-commerce live streaming has become the 
most popular live streaming in many countries (CINIC, 2020), our work aims to 
identify the challenges and opportunities of the current LSC systems and inspires 
better design of live streaming affordances of online shopping activities.
708

## TRANG 9

How Live Streaming Changes Shopping Decisions in E‑commerce:…
3  Methods
The research questions that we study in this paper are about how consumers are 
influenced by live streaming and streamers in their decision-making process. We 
conduct a mixed-methods research methodology to explore consumers’ experi-
ences and understandings in LSC. The study has been approved by the Institu-
tional Review Board (IRB) at the City University of Hong Kong where the study 
was conducted.
3.1  Data Collection: Online Survey
The first step of our study is a survey study with LSC consumers. We developed 
an online survey with both multiple-choice questions and open-ended questions 
to explore consumers’ shopping experiences in LSC. The survey was organized 
in English and then translated into Mandarin by two native Mandarin speakers 
in the research team. We recruited participants who have experience in LSC in 
China. We used services from wj.qq.com, i.e., a firm specializing in recruiting 
study participants. The survey was active for 3 weeks in June of 2020, and a total 
of 240 responses were collected. The expected time for completing the survey 
was 10-15 minutes. Each participant received 15 CNY as reward. At the end of 
the survey, we asked respondents whether they would like to attend post-survey 
interviews. If so, they left their contact information.
3.2  Data Analysis: Online Survey
After collecting survey data, we created a statistic with the basic information of 
participants, including age, location, times of watching per week, money spent 
per month and months of experience for watching, and their usage of different 
platforms. 240 participants completed our online survey in total and the average 
finishing time was 10 minutes 14 seconds. Most of the participants were young 
or middle-aged people, in the age group of 18-40 (94.6%) with a concentration 
in 26-30 (38.3%). Those results are consistent with the statistics of LSC users 
and previous research (Lu et al., 2018) on live streaming in China. 86.3% of the 
participants have participated in LSC at least once per week and 79.6% of them 
spend more than 100 CNY on buying products from LSC per month, demon-
strating their rich experiences in LSC. More than half (54.2%) of the participants 
have used LSC for half to one year, which demonstrates the rapid development of 
LSC since 2019.
The development of LSC is not limited to a single platform. More than half of 
our respondents have used several different LSC services on Taobao (88.33%), 
JD (56.83%), TikTok (67.5%) and Kuaishou (51.67%). These four platforms 
fall into two completely different categories: e-commerce platforms and video/
streaming platforms. Previous studies indicated that Chinese live streaming prac-
tices are only conducted through video/streaming platforms (Lu et  al., 2018, 
709

## TRANG 10

Y. Wang et al.
2019). However, our result suggests that LSC has also been developed on e-com-
merce platforms.
Respondents also addressed their preferences on LSC and their perception of 
different streamers and platforms in open-ended questions. We used an open cod-
ing method (Corbin and Strauss, 2014) to analyze these responses. We classified 
factors that influenced their online shopping decisions at different stages. Native 
Mandarin-speaking authors coded all responses individually and met several 
times to discuss the agreement on the final results. All codes were translated into 
English and discussed by the research team.
3.3  Post‑Survey Interviews
To get a deeper understanding of our research questions, we conducted post-
survey interviews using WeChat voice calls. From 213 survey participants who 
would have liked to join the interview study and had left their contact informa-
tion, we randomly sampled 20 users. Sixteen of them replied to our interview 
invitations between June and July 2020. Interviews were conducted in Mandarin, 
audio-taped, and transcribed by three native Mandarin speakers in the research 
team. Each interview took 30-45 minutes, and each participant received a 100 
CNY honorarium for their time. Based on the online survey data analysis, the 
interview questions aimed to explore more insightful understandings of the affor-
dances and challenges of live streaming and streamers in their LSC experiences. 
We asked them to describe their LSC shopping experience in detail, including 
the information they received in LSC, their perceptions about this information, 
and their understanding of the products, merchants, and streamers when they 
made the shopping decision.
We followed the code scheme as in the data analysis of survey data. Native 
Mandarin-speaking authors coded all responses individually. When there were 
new themes observed by researchers, the research team came together to dis-
cuss the agreement on the final results. Finally, we summarized findings of each 
research question, as influential factors in shopping decision-making.
4  Affordances and Challenges of Live Streaming
Live streaming technology provides synchronized multisensorial communication 
between merchants and consumers. Consumers can see the action of merchants 
and hear the merchants’ voices, while merchants can read text messages sent by 
consumers in real-time. We find that live streaming enables merchants to enhance 
consumers’ perceptions of products and online stores at the stages of information 
search and deciding to purchase. Meanwhile, live streaming affords consumers’ 
pleasure and arousal, which actively incentivizes impulse buying in LSC. On 
the other hand, since the communication in LSC is one-to-many, the information 
710

## TRANG 11

How Live Streaming Changes Shopping Decisions in E‑commerce:…
received by shoppers has not been personalized, thus introducing challenges in 
shopping efficiency.
4.1  Afford Evaluations on Products
Around one third (36.3%) of the respondents considered that the products sold on 
LSC have good qualities and 41.7% of the respondents agreed that they bought 
products in LSC because they think that these products are useful to them. To 
better understand why people consider the products they bought in LSC are use-
ful and have better qualities, we explore how they generate such perceptions dur-
ing their shopping experiences.
Accessibility of  Authentic Information  First, the accessibility for acquiring 
authentic information has been supported in LSC. Merchants can provide an 
authentic demonstration of the products in live streams (Wongkitrungrueng and 
Assarut, 2018). Live streaming transmits their expressions and actions in real-
time, in a way that cannot be pre-processed or edited prior to being presented, 
and consumers can access the actual appearance and applications in real usage 
scenarios, such as clothes, cosmetics, etc. (Tang et  al.,  2016). Therefore, 
live streaming enables consumers to get more authenticate information from 
merchants: “Now, if I want to buy clothes, I will definitely look for a LSC 
store so that I can ask the merchants to put the cloth on for me. You know, the 
description of clothes on Taobao only contains some pictures with professional 
models, which is so fake, and I cannot make decisions based on that. I want to 
see the actual fit, like I am trying the cloth in the fitting room.” (P13) On top 
of using the products in live streaming to deliver authenticity to consumers, 
merchants can also show the producing environments to consumers in LSC. 
These presentations provide viewers with a better understanding of products: 
“I knew that we have such a beautiful village in Yunnan through LSC. The sky, 
the water, the mountain are so beautiful from their lens. I want to buy products 
from them because I know how good the environment is, and it definitely 
satisfies my demand for organic food.” (P9)
Targetability of  Information Collection  It is not always the case that the more 
information the consumers gets, the better. The second affordance that we 
explore in LSC is whether consumers can receive the information precisely. 
Although the information of products listed on the traditional e-commerce 
platforms can cover the majority of problems that consumers might have, 
each consumer may have different needs for information. In LSC, merchants 
can immediately know consumers’ needs for the products and adjust their 
presentations based on audience real-time feedback. Consumers do not need to 
find the information they need from a large number of texts and images on the 
website but can get an accurate response from merchants directly: “Last time I 
711

## TRANG 12

Y. Wang et al.
bought a special cleaning tool. It was my first time to know this tool, so I was 
worried about whether its size is too large and where to place it. The merchant 
answered all my questions patiently and showed me how to use it. It is very nice 
because I know this is something that I can use based on her explanation.” (P10) 
In the shopping experience of P10, she cares more about the size and installment 
of the cleaning tool than other information. Through visual demonstration and 
real-time communication, merchants can efficiently solve her concerns, which 
increases the efficiency for P10 to make shopping decisions.
With such authentic and efficient information exchange in LSC, more and 
more consumers consider LSC as their first choice of online shopping: “It 
should be said that I have developed a habit now, that is, when I want to buy 
something, I will first go to Taobao Live. If I have not found a LSC, I will 
then search for it on other e-commerce platforms.” (P8) P2 considers he saves 
money by using LSC because he is more satisfied with products he bought in 
LSC than other e-commerce platforms: “Sometimes, I do not know how to use 
the product if I buy it from Taobao. It is a waste of money. Now I feel much 
better (from LSC) because streamers will show me how to install it, use it and 
the precautions, etc.” (P2)
Reliability of Peer Review  Lu et al. (2018) and Cai et al. (2018) both mentioned that 
one advantage of LSC is that it enables consumers to obtain reliable information 
on products from other consumers in the same LSC because they trust peers 
more than merchants. Although this argument sounds reasonable, this was 
not considered as an advantage of LSC for most respondents. Only 17.5% of 
the participants trust other consumers’ comments on products. In contrast, 
participants do not think reviews from other consumers are trustworthy, 
especially for positive ones: “It is full of shuijun2 of merchants repeating good 
reviews. (Interviewer: Why do you think those comments are from shuijun?) 
It is so obvious because everyone repeats the same words. Useful information 
was quickly overwhelmed. These comments distract me from watching the 
live stream. I always turned the comment area off because it is annoying and 
useless.” (P1) Some interviewees thought these comments are even less 
reliable than comments on traditional e-commerce platforms: “The comments 
on Taobao websites are only written by people who have bought the products, 
which is quite objective. Anyone can write comments in live streams. I do not 
trust them.” (P5) The experiences of our interviewees suggest that information 
exchanges between unknown consumers in LSC do not help much with online 
shopping activities. Consumers have difficulties in distinguishing useful 
comments from excessive fake information.
2  A group of internet ghostwriters paid to post online comments with particular content.
712

## TRANG 13

How Live Streaming Changes Shopping Decisions in E‑commerce:…
4.2  Afford Evaluations on Online Stores
The affordance of live streaming does not limit with the products themselves. 
In fact, live streaming also supports consumers’ evaluations for merchants them-
selves. Consumers’ perception of the online store has been enhanced by satisfy-
ing customer services, which encourages consumers to purchase products with 
the merchants.
Connectivity Between Merchants and Consumers  For example, live streaming enables 
merchants to form personal relationships with their consumers and strengthen the 
ties with them, especially for small merchants. Because there are not many con-
sumers participating in LSC of small merchants at the same time, merchants can 
have more interactions with the consumers and thus provide more personalized 
suggestions, which creates a more enjoyable shopping environment for consum-
ers as in offline stores. P10 had such a good experience in LSC: “At the end of 
2018, one of my friends recommended a merchant who sells clothes. Some of 
our friends joined that live stream every day for at least one week. It is not a 
big merchant, so she knew us quickly. It is delightful because the merchant can 
recommend us clothes according to our preference. Each of us bought at least 
ten clothes from that merchant.” (P10) With such individual interactions with 
the merchant, P10 and her friends enjoyed good online shopping experiences 
and were satisfied with products they bought from the merchant. Social rela-
tionships between merchants and consumers are formed through live streaming 
communication.
Expandability of Additional Services  Furthermore, some merchants provide additional 
services to attract and satisfy consumers. For example, some cosmetic merchants 
teach makeup skills in LSC: “Makeup requires some special skills. For example, 
if I use this beauty egg in different ways, I will have different looks. … It is not 
that I do not know how to use it. It is a special skill (she taught us). If we don’t 
understand how she made it, she will repeat until it is clear to us.” (P6) P6 felt 
that she is not only attracted by the products sold by the merchants, but also the 
extra helps, which improves her understanding of the products she bought and 
experiences in using the products.
4.3  Afford Pleasure and Arousal
Arousal is considered as an affective property (dimension) ranging from sleep to 
frantic excitement (Mehrabian and Russell, 1974) and pleasure refers to valence 
of the affective state (Mehrabian, 1996). We find that the competition elements 
among consumers in live streaming leads to a high arousal, which enhances 
impulsive buying (Herabadi et al., 2009; Liao et al., 2016), while beneficial and 
713

## TRANG 14

Y. Wang et al.
rewarding elements improve the pleasure of consumers in LSC and moderate 
shopping decisions (Wirtz et al., 2007).
Competitions Among Consumers Increase Arousal  To increase the engagement of con-
sumers, competitive games have been introduced to LSC. For instance, streamers 
may set explicit rules for shopping activities, e.g., the first buyers will earn addi-
tional prizes. Such competitions have positive influences on arousal during the 
decision-making process. P1 considers that sometimes she does not really want 
to buy the product but just feel it is interesting to get limited edition products: 
“He counted down from 5 to 1 before the product became available to everyone. 
I know a lot of people want to buy it, so I feel very happy if I am under the first 
one hundred people to get that product. Maybe I was not really interested in that 
product. But I earned happiness from beating others.” (P1)
Benefits and Rewards Increase Pleasures  Sending virtual gifts to streamers is consid-
ered as a popular activity in live streaming (Lu et al., 2018, 2019; Wang et al., 
2019; Wohn et al., 2018). However, in LSC, we observe an opposite phenom-
enon, such that streamers provide benefits to consumers in LSC. For example, 
streamers hold lottery activities in LSC.
Such beneficial and rewarding elements in LSC have increased consumers’ 
pleasure and attracted a lot of consumers’ attention: “She holds many lottery 
activities every day. When a lottery activity happens, the chatting space is full of 
lottery messages. Almost everyone (also those not interested in her LSC) is par-
ticipating in.” (P13) The experiences of P13 indicate that these benefits and gifts 
encourage more people to join LSC or stay in LSC for a longer time after their 
online shopping activities. Moreover, pleasure generated by rewarding positively 
influence consumers’ goodwill and trust in the streamers, while they are more 
prone to be influenced by streamers in shopping decisions: “I think he is quite 
generous and often sends gifts to us, the audience. I feel like our relationship is 
like a friend, so I feel he won’t cheat us and sell us low-quality products.” (P7)
4.4  Challenges of Live Streaming in LSC
Although live streaming has supported the decision-making process in online 
shopping activities from several perspectives, we note that there are still chal-
lenges that need to be addressed, which greatly affected the development and sus-
tainability of LSC.
The first significant challenge is related to the one-to-many communication. 
Although the communication mechanism can improve the efficiency of stream-
ers to deliver information to consumers, the information received by different 
users is identical. Time-saving is considered as a decisive factor in the emer-
gence and prosperity of the shopping paradigm (Chen et al., 2014; Koyuncu and 
714

## TRANG 15

How Live Streaming Changes Shopping Decisions in E‑commerce:…
Bhattacharya, 2004; Van der Heijden et al., 2003). For experienced consumers, 
their time costs are relatively high because the information delivered in LSC is 
always redundant while they have already received the same information in pre-
vious practices. Almost all of our interviewees mentioned that the frequency of 
participation in LSC had been gradually decreasing: “I use less and less LSC for 
online shopping. I stared on my phone a whole night but only bought very few 
things. I feel it is a waste of my time.” (P16) Apart from the one-to-many com-
munication mechanism, the repetition of products selling in LSC also decreases 
consumers’ willingness for shopping in LSC. Most streamers hold LSC at least 
three times a week, selling dozens of items each time, which results in recom-
mending more than 500 products per month. Therefore, ome products will appear 
in LSC with a higher frequency, far beyond the frequency of consumers’ repur-
chase of them, which distracts the efficiency of the information containing in 
each LSC.
5  Affordances and Challenges of Intermediaries in LSC
Live streaming does not only serve as a decision support system in LSC, but also 
enables market intermediaries to participate in the e-commerce practices. Many 
LSC streamers do not own their online stores. Instead they sell products through 
live streaming during a specific time slot and consumers can directly buy the 
products in their LSC.
Compared to merchants, LSC streamers have two distinguishable differences. 
First, the items they sell in LSC vary for each live streaming and consumers do 
not know at what specific time they will sell the products. Second, streamers 
have schedules for their presentations of different products. Therefore, consum-
ers can only acquire information about a product and decide whether to buy it in 
LSC during a certain period of time. As intermediaries in the market, streamers 
directly communicate with consumers in their LSC. In other words, streamers 
control the communication channel with consumers in their LSC, while mer-
chants cannot exchange information with consumers through live streaming in 
the presence of streamers.
LSC streamers can be mainly classified into two categories: professional 
streamers and crossover streamers. Professional streamers refer to those who 
do not participate in live streaming activities other than LSC, while crossover 
streamers were already active in other types of live streaming before they con-
ducted LSC practices. Although there might be some overlaps between these two 
categories, the main difference between professional streamers and crossover 
streamers is whether their followers are attracted by LSC or other live streaming 
performances.
715

## TRANG 16

Y. Wang et al.
In this section, we aim to explore how streamers influence the consumer deci-
sion-making process at different stages. The participant of market intermediaries 
introduces additional affordances in the online shopping systems. We focus on 
three stages where streamers are most influential, i.e., shopping need awareness, 
decision making, and post-purchasing evaluation.
5.1  Stimulability for shopping needs awareness
Some consumers may not have a clear shopping awareness when they partici-
pate in LSC. The majority of consumers (58.5%) participate in LSC because 
they want to buy something recommended by streamers but without a clear goal. 
Therefore, streamers arouse the shopping need awareness of consumers in LSC. 
According to our respondents’ replies, we summarize five different scenarios to 
examine the stimulability for shopping needs awareness.
Attending LSC Practices  Streamers first attract consumers to participate in their 
LSC practices and then make them interested in the products they sell. Crosso-
ver streamers have significant advantages at this stage. Because they have accu-
mulated considerable fame and knowledge in their specialized fields, consumers 
have a natural belief in their specialization. P5 is a sports fan and has followed 
many sports streamers on live streaming platforms. He attends LSC because of 
his recognition of his favorable streamers: “I like sports, especially basketball. 
My favorite streamer on TikTok is Junge, and I have followed him for a long 
time. He sometimes sells basketball jerseys in LSC. I often buy basketball equip-
ment from him because I trust him in sports.” (P5) On the contrary, crossover 
streamers are only recognized in the specific domain. The majority of products 
selling through LSC have to be related to their expert fields. Their followers may 
not trust crossover streamers when they sell something far away from their exper-
tise: “I do not buy other products from her (a make-up streamer). I don’t trust the 
snacks she recommended. I tried it once and found it does not taste good. I prefer 
buying snacks from another streamer.” (P16)
Resonating with Consumers  After leading consumers into live streaming, streamers 
introduce the products they sell to raise consumers’ shopping need awareness. 
LSC streamers use products they sell to conduct performances. For example, 
they eat food during LSC and sell the same product to their audience; or make up 
with the cosmetics they sell in LSC. The audience may have a high recognition 
of items that are used in live streaming performance (Anjani et al., 2020). When 
asked about the most impressive LSC experience, some respondents of our sur-
vey mentioned that they buy products when looking at their live streaming per-
formance with the products: “I bought rice noodles in a mukbanger’s LSC. Wow, 
I looked at how the streamer ate the noodles and heard the sound he made. The 
716

## TRANG 17

How Live Streaming Changes Shopping Decisions in E‑commerce:…
noodles seemed very, very delicious! Each package has a large volume as well, 
so I bought the noodles right away.”(S226)
Improving Online Shopping Engagement  Moreover, streamers invite consumers 
to participate in their performances and create a stronger sense of engagement 
of the consumers to enhance their interests in the products. For example, when 
selling food, streamers follow consumers’ suggestions to taste the food they are 
interested in. Consumers can express which products they would like to watch 
streamers eat and build a stronger sense of identity with the food when watch-
ing live streams (Choe, 2019). This also happens when streamers make up with 
beauty products. P6 felt excited when the streamers interact with her during the 
live streaming performance: “He (a make-up streamer) will ask audiences which 
lipstick we would like him to try first. If he tries the color that I recommended, I 
feel very happy. I cannot stop buying it (the lipstick he tries) even if I have a lot 
of lipsticks.” (P6)
Non‑intentional Shopping Awareness in  LSC  Sometimes consumers do not have a 
clear goal for shopping when they watch live streams. Streamers may influence 
consumers’ shopping decisions because they offer useful and interesting items 
to consumers. P16 tells us that when she felt boring, she would open LSC and 
watch the performance of streamers. Although she does not have a specific desire 
to shop, she occasionally places orders with the streamers: “Sometimes they sell 
toilet paper at a very low price. I asked myself: why don’t I buy it? I always need 
it anyway. So I bought it for no other reason, just for the low price.” (P16)
Non‑LSC Practices  Apart from enhancing shopping need awareness during LSC, 
some crossover streamers also utilize consumers’ interest in props that they use 
during their non-LSC live streaming practices to sell products. Because these 
props always appear in their performance, consumers’ recognition of the props 
will gradually deepen as they favor the streamers’ performance: “I usually learn 
how to bake from her live streams, and I felt that her supplies were very profes-
sional and good. That time she sold the baking tools she was using in the LSC, so 
of course, I bought some.”(S125)
5.2  Influenceability on Shopping Decisions
In LSC, the most information consumers acquire is from streamers, while their 
evaluations on the products are influenced by how much they trust from the 
information resource. Meanwhile, their evaluations of streamers also determine 
their final decisions of purchase. In this subsection, we explore how the identity 
of streamers influences consumers’ evaluation of products and themselves.
LSC streamers may not be bonded with other merchants. Because the iden-
tity of streamers and the identity of merchants can be independent, consumers 
717

## TRANG 18

Y. Wang et al.
perceive that streamers can provide objective opinions on the products that 
they sell. Our survey respondents consider these perceived objective opinions 
bring them good online shopping experiences: “Last time I bought a laptop 
from him. He did not only say how good the laptop is but also analyzed its 
weakness and whether it is suitable for us, which made me understand the 
advantages and disadvantages. It is more useful than those merchants only 
tell you it is good.” (S166) If consumer perceive that streamers present unbi-
ased stances, streamers’ words are convincing to consumers when deciding 
whether and what to buy.
Moreover, some streamers utilize “Lianmai” (Li et al., 2019) function to 
conduct co-selling practices, where audiences of two streamers can watch 
the performance of two streamers in the same interface. In co-selling, one 
streamer does not sell anything, while the second streamer is a merchant. 
The first streamer brings all her audience to LSC, watches how the merchant 
presents the product, and negotiates with the merchant about the product’s 
price. The streamers always perform as represents of consumers to persuade 
the merchant providing a better price or offering extra gifts: “The reason that 
I liked him is he always fights for his audiences with other streamers. I could 
feel that he really wanted us all to be able to buy the product at the lowest 
possible price.” (S32) In the form of co-selling in LSC, streamers companion 
with consumers during the entire decision-making process and perform as 
the representative of the consumers to negotiate with the seller, which makes 
consumers feel like a more immersive online shopping experience.
5.3  Reliability of Post‑Purchasing Services
As the third party in LSC between merchants and consumers, streamers also 
involve in the post-purchasing evaluation stage of the consumer decision-
making process, which improves the reliability of such services (Adjei et al., 
2010; Archer and Yuan, 2000; Salam et al., 2005; Singh, 2002; Sutanonpai-
boon and Abuhamdieh, 2008).
Some streamers provide additional after-sales services paralleling with 
merchants, which improves consumers’ recognition of them and encourages 
them to conduct online shopping practices with the streamers in the future. 
Streamers act as mediation agents to coordinate or solve conflicts between 
consumers and merchants: “He (a streamer) had a collaboration with the mer-
chant, and he promised that the merchant would send us a lipstick of the most 
popular color as a gift for every order. But the merchant sent some random 
colors to us. I feel I was cheated and contacted the customer service of the 
streamer. They helped me contact the merchant to send me the correct gifts.” 
(P8)
718

## TRANG 19

How Live Streaming Changes Shopping Decisions in E‑commerce:…
By playing as a neutral third party helping consumers solve after-service 
problems, streamers make consumers more assured of shopping through 
LSC. Although such after-sales services cannot directly influence consum-
ers’ shopping decisions of the previous shopping decisions, the help provided 
by streamers can strengthen consumers’ recognition of the streamers, which 
will positively influence future shopping decisions in LSC with the same 
streamers.
5.4  Challenges of Streamers in LSC
Although streamers in LSC provide various affordances in consumers’ decision-
making process, we also find our respondents perceive challenges of the involve-
ment of streamers in LSC.
First, some streamers encourage consumers to perform impulsive buying. For 
example, they might repeat how useful the product is, how cost-effective the 
product is, and how a limited number of items are available, to invoke consum-
ers’ desire to buy the product. P8 considers that she is easily influenced by such 
incitement :“He keeps repeating that it is the best offer that we can have forever, 
i.e., the first one is the original price, the second item is half price, and the third 
one is free, etc. He lets me feel that if I don’t buy it, I am an idiot and will lose 
money.” (P8) When consumers are immersed in live streaming, they do not have 
time to look for information outside the live stream, which may cause a lot of 
irrational shopping behaviors.
Second, some coalitions may exist between streamers and merchants, while 
streamers may deliver deceptive information to consumers. For instance, in the 
form of co-selling in LSC, rather than authentically helping customers make bar-
gains, the streamers conspire with merchants to deceive consumers: “It seems 
that they were just performing for us. Two streamers spoke very loudly to attract 
my attention. They quarreled with each other and kept saying something like, 
‘The original price was more than 100. Now! Only for my audience, the cur-
rent price is 9.9!’ I just felt that they were deceiving me. It is the same perfor-
mance every time.” (P3) Consequently, these streamers may lose credibility from 
consumers.
In LSC, streamers dominate the entire shopping process. Consumers’ percep-
tion of the selling products is based on how streamers present products. Mean-
while, the entire shopping experience in LSC is coherent, in which consumers 
complete the whole process from receiving information to purchasing products 
within the same interface. Therefore, external information from a third party can-
not affect user perception during the period, while the information provided by 
streamers has been gradually enhanced. All these factors contribute to the fact 
that streamers are powerful in LSC, and they may deliver fake information to get 
extra benefits from consumers (Yi, 2020).
719

## TRANG 20

Y. Wang et al.
6  Discussion
In this paper, we analyze the purchase decision-making process of consumers 
in LSC. LSC has two unique features compared to other e-commerce models: 
the live streaming as a decision support system, and streamers as market inter-
mediaries. We find that the decision support system improves the evaluation of 
products and online stores at the information search and the alternative evalu-
ation stages, while the market intermediaries influence consumers at the shop-
ping need awareness, deciding to purchase, and the post-purchasing stages. On 
top of understanding the affordances and challenges of current LSC, we pro-
ceed to discuss the uniqueness of LSC that distinguishes it from other e-com-
merce models, and implications for the LSC service providers and research 
communities.
6.1  Offline‑like Online Shopping Experiences
Online shopping has many advantages compared to offline shopping (Kataweta-
waraks and Wang,  2011). For example, online shopping is considered more 
convenient (Wang et  al., 2005), because it provides services with consumers 
24 hours a day, 7 days a week and avoids crowds and waiting lines. Moreover 
e-commerce offers consumers more variety of available products and services 
(Lim and Dubinsky, 2004). Compare to traditional e-commerce, LSC provides 
offline-like online shopping experiences with consumers regarding to the follow-
ing perspectives: intangibility of products and social contact.
6.1.1  Intangibility of products
Consumers are less likely to buy some types of products because they can not 
try or examine the actual products through the online channel (Comegys et al., 
2009), especially for the products such as clothes, which have significantly dif-
ferent effects by observing from e-commerce websites and seeing in the stores. 
Moreover, the information provided by the e-commerce websites always cannot 
meet the expectation of consumers when they make purchasing decisions (Liu 
and Guo, 2008).
LSC optimizes the intangibility of products from both the technical per-
spective and the human perspective. Live streaming technology delivers more 
informative messages to consumers, including images, actions, and voices. With 
the information of these different senses delivered by live streaming, consumers 
may imagine the actual effect when using the products. They can better exam-
ine the products like clothes and are now willing to purchase these products in 
720

## TRANG 21

How Live Streaming Changes Shopping Decisions in E‑commerce:…
LSC. Although live streaming cannot provide the same shopping environments 
as offline stores, it optimizes the online shopping experience, both visually and 
audibly.
Moreover, although consumers cannot directly see, hear, feel, touch, smell, or 
try the product themselves in LSC, they can empathize with the streamers who 
use the products. With the development of trust and recognition of streamers, 
consumers can evaluate the products from the real-time reactions and feedback 
from the streamers through live streaming, which decreases the intangibility of 
online shopping.
6.1.2  Social Contact
Both the assistance from professional salespersons and opinions from other 
consumers are helpful for people to make shopping decisions (Prasad and 
Aryasri, 2009). By establishing real-time communication with merchants, intro-
ducing streamers, creating shopping environments with many consumers, and 
encouraging interactions with acquaintances, the social contact of consumers has 
been greatly enriched in LSC compared to other traditional e-commerce.
First, consumers can interact sufficiently with merchants, streamers and other 
consumers during the online shopping practices. Based on the affordance of 
the combination with hot media (streaming image) and cold media (text chat) 
(Hamilton et al., 2014), consumers can actively express their doubts, needs, and 
opinions to streamers and other consumers as well, to construct an interactive 
online shopping environment and develop shared histories. The various interac-
tions within LSC can be considered as a major difference compare to TV shop-
ping channels. Although TV shopping also supports the parasocial interaction 
between consumers and hosts, LSC enhances this interaction with different LSC 
affordances and even extends to the parasocial interaction between different 
consumers.
Second, streamers can easily influence consumers’ emotions in LSC. Apart 
from the affordances of arousal and pleasure that we reported in Section 4.3, con-
sumers also engage in live streaming performances and other entertaining activi-
ties in LSC. Their online shopping practices have changed from pure purchas-
ing to comprehensive commercial and entertainment practices similar to offline 
shopping.
Third, streamers also strengthen their relationships with consumers outside 
LSC, such as after-sales services provided by streamers and other live streaming 
practices conducted by crossover streamers. Moreover, because LSC and stream-
ers may become common topics between people who have close relationships, 
their recognition of LSC has been deepened, and they are more likely to join in 
LSC together.
721

## TRANG 22

Y. Wang et al.
6.2  Implications
Although we take the online shopping activities in Chinese LSC as an example in 
this paper, we do not aim just to report specific content in China. In this subsec-
tion, we discuss the implications from three perspectives based on our findings 
and beyond the specific content, namely from service providers and researchers.
6.2.1  LSC Service Provider
Since live streaming is a novel decision support system in online shopping, there 
are still challenges in the current LSC system. Therefore, we discuss the design 
implication of LSC systems from two perspectives: providing various function-
alities for different users and providing external choices. Moreover, we discuss 
more general implications regarding the development of LSC.
Design Implications  First, as experienced users perceive that they receive repeated 
information in LSC, which decreases their shopping efficiency, LSC service pro-
viders may consider consumer triage to provide multiple modules in parallel to 
meet the different needs of consumers. For example, LSC can set two phases for 
placing the order before and after the introduction, where experienced users can 
save time to buy products efficiently, while new consumers can wait until getting 
enough information for making shopping decisions. The behavior of consumers 
in the early phase can also be used as references for new consumers. The pur-
chase data might be more objective than text messages sent by other consumers 
in LSC. Similarly, LSC service providers may also consider to share the informa-
tion of the current on sale products on other social media or pushing notifications 
in real-time to enable experienced consumers to participate in LSC at a precise 
time. They can skip the time of repeated products or something they are not inter-
ested in. Thus, consumers can save more time without participating in a low-
informative LSC period.
Second, as we discussed in Section  4.1, in current LSC, consumers cannot 
take peers evaluation on products as helpful eWOM for shopping decisions. 
Therefore, LSC may introduce external information to help consumers build an 
objective view of products and eliminate streamers’ dominance. For example, 
LSC can display information from external resources in the interface, such as 
consumers’ reviews on e-commerce platforms or discussions about products on 
social media. Consumers will have access to this third-party information from 
different sources during the shopping process and be more rational when making 
shopping decisions.
General Implications  LSC has become a popular e-commerce model in China. 
However, it has not been fully accepted in other countries. We explore two main 
722

## TRANG 23

How Live Streaming Changes Shopping Decisions in E‑commerce:…
reasons for the success of LSC in China to inspire the future development of LSC 
all over the world.
First, Chinese users have developed the habit of using live streaming (Lu et al., 
2018). As the most popular entertaining applications, streaming/video platforms 
have taken up most Chinese users’ leisure time (CINIC, 2020). Therefore, we 
may expect the future development of LSC on streaming/video platforms in other 
countries as well if they can build their own e-commerce services. Although such 
a combination of streaming/video platforms and e-commerce content encour-
ages users to adapt LSC, we also notice the potential negative impact of com-
mercial content on non-intended users on video/streaming platforms. As part 
of video/streaming platforms, LSC will be pushed to users when browsing non-
commercial content based on personal information they share on social media 
(Qin and Jiang, 2019). Even though some consumers think it is enjoyable to shop 
in a relaxing environment, some other impulsive consumers might be seriously 
influenced by LSC and conduct irrational or emotional shopping behavior (Eastin 
et al., 2016). On the other hand, the system algorithm may not fully understand 
user behavior on the video/streaming platform, and the recommendation might 
not be accurate, which could be harmful to consumers (Brockell, 2018). There-
fore, these non-e-commerce platforms should allow consumers to opt out of LSC 
from the platform.
Second, shopping sites are very thoroughly integrating live streaming features. 
As we have shown in Figure 1, e-commerce platforms actively guide users to 
join LSC from the traditional e-commerce platform and even offer additional dis-
counts. Consumers are prone to accept live streaming services with such repeated 
experiences. For instance, Aliexpress has attracted global users to participate in 
LSC with their attempts (Wei, 2020). However, other more popular e-commerce 
platforms have not fully adapted LSC, which may postpone the development of 
such an e-commerce model over the world.
6.2.2  Research Community
Our paper focuses on the decision-making process of consumers in LSC. We 
obtain many new observations and findings, which help people have a deep under-
standing of LSC. This study raised, but did not answer, many interesting and 
important questions that we commend to future researchers (including ourselves):
•	
What are the differences in consumer practices in LSC on e-commerce plat-
forms and streaming platforms? How do consumers perceive the affordances 
on different platforms?
•	
How do streamers interplay and negotiate with merchants? How do they sell 
products with a lower price of products than merchants?
723

## TRANG 24

Y. Wang et al.
•	
How do streamers manage their relationships with their consumers online 
and offline?
LSC has become an interdisciplinary topic of computer science, business, man-
agement, psychology, and sociology. Because of the limitation of our data (we only 
collect data from experienced consumers but not other stakeholders in LSC), we 
may not explore all aspects in this paper. However, we expect future work to contrib-
ute to understanding this increasingly important topic from different perspectives.
7  Conclusion
In this paper, we study an emerging socio-technological phenomenon, i.e., LSC 
in China, to understand how consumers’ shopping decisions are influenced when 
live streaming combines e-commerce. We examine the new e-commerce model 
from the technical and human perspectives. Our work does not only provide 
insights into how LSC becomes successful but also considers the current limita-
tions of LSC. We provide implications to address existing issues and inspire LSC 
service providers, market intermediaries and research communities.
Supplementary Information  The online version contains supplementary material 
available at https://​doi.​org/​10.​1007/​s10606-​022-​09439-2.
Funding  Open access funding provided by Swiss Federal Institute of Technology 
Zurich
Declarations 
Conflict of Interests  The authors declared that they have no conflict of interest.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 
International License, which permits use, sharing, adaptation, distribution and 
reproduction in any medium or format, as long as you give appropriate credit to 
the original author(s) and the source, provide a link to the Creative Commons 
licence, and indicate if changes were made. The images or other third party mate-
rial in this article are included in the article’s Creative Commons licence, unless 
indicated otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not permitted 
by statutory regulation or exceeds the permitted use, you will need to obtain per-
mission directly from the copyright holder. To view a copy of this licence, visit 
http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
724

## TRANG 25

How Live Streaming Changes Shopping Decisions in E‑commerce:…
References
Aakhus, Mark (2007). Communication as design. Communication Monographs, vol. 74, pp. 112–117.
Adjei, Mavis T.; Stephanie M. Noble; and Charles H. Noble (2010). The influence of c2c communications 
in online brand communities on customer purchase behavior. Journal of the Academy of Marketing 
Science (JAMS), vol. 38, pp. 634–653.
Agnihotri, Raj; Adam Rapp; and Kevin Trainor (2009). Understanding the role of information communica-
tion in the buyer-seller exchange process: antecedents and outcomes. Journal of Business & Industrial 
Marketing (JBIM), vol. 24, pp. 474–486.
Alba, Joseph; John Lynch; Barton Weitz; Chris Janiszewski; Richard Lutz; Alan Sawyer; and Stacy Wood 
(1997). Interactive home shopping: consumer, retailer, and manufacturer incentives to participate in 
electronic marketplaces. Journal of Marketing (JM), vol. 61, pp. 38–53.
Alperstein, Neil M. (1991). Imaginary social relationships with celebrities appearing in television commer-
cials. Journal of Broadcasting & Electronic Media (JoBEM), vol. 35, pp. 43–58.
Anjani, Laurensia; Terrance Mok; Anthony Tang; Lora Oehlberg; and Wooi Boon Goh (2020). Why do 
people watch others eat food? an empirical study on the motivations and practices of mukbang view-
ers. In: CHI’20: Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, 
Honolulu HI USA, 2020. New York: Association for Computing Machinery, pp. 1–13.
Archer, Norm; and Yufei Yuan (2000). Managing business-to-business relationships throughout the e-com-
merce procurement life cycle. Internet Research, vol. 10, pp. 385–395.
Brockell, Gillian (2018). Dear tech companies, i don’t want to see pregnancy ads after my child was still-
born. Article. The Washington Post, December 2018. https://​www.​washi​ngton​post.​com/​lifes​tyle/​
2018/​12/​12/​dear-​tech-​compa​nies-i-​dont-​want-​see-​pregn​ancy-​ads-​after-​my-​child-​was-​still​born/.
Cai, Jie; and Donghee Yvette Wohn (2019). Live Streaming commerce: Uses and gratifications approach to 
understanding consumers’ motivations. In: HICSS’19: 52nd Annual Hawaii International Conference 
on System Sciences, Grand Wailea, Maui, Hawaii, USA. Washington D.C.: IEEE Computer Society, 
pp. 2548–2557.
Cai, Jie; Donghee Yvette Wohn; Ankit Mittal; and Dhanush Sureshbabu (2018). Utilitarian and hedonic 
motivations for live streaming shopping. In: TVX’18: Proceedings of the 2018 ACM international 
conference on interactive experiences for TV and online video, SEOUL Republic of Korea, June 
26–28, 2018. New York: Association for Computing Machinery, pp. 81–88.
Cao, Hancheng; Zhilong Chen; Fengli Xu; Tao Wang; Yujian Xu; Lianglun Zhang; and Yong Li (2020). 
When your friends become sellers: An empirical study of social commerce site beidian. In: ICWSM 
20’: Proceedings of the International AAAI Conference on Web and Social Media, Atlanta, Georgia, 
USA, 2020, Vol. 14. Menlo Park, California: Association for the Advancement of Artificial Intelli-
gence, pp. 83–94.
Cao, Hancheng; Zhilong Chen; Mengjie Cheng; Shuling Zhao; Tao Wang; and Yong Li (2021). You recom-
mend, i buy: How and why people engage in instant messaging based social commerce. Proceedings 
of the ACM on Human-Computer Interaction (PACMHCI), vol. 5, pp. 1–25.
Chakravarty, Anindita; Alok Kumar; and Rajdeep Grewal (2014). Customer orientation structure for inter-
net-based business-to-business platform firms. Journal of Marketing, vol. 78, pp. 1–23.
Chen, Yuxin; Ganesh Iyer; and V. Padmanabhan (2002). Referral infomediaries. Marketing Science (MS), 
vol. 21, pp. 412–434.
Chen, Jun; Xiao-Liang Shen; and Zhen-Jiao Chen (2014). Understanding social commerce intention: A rela-
tional view. In: 2014 47th Hawaii International Conference on System Sciences, Waikoloa, HI, USA, 
6–9 Jan. 2014. Washington D.C.: IEEE Computer Society, pp. 1793–1802.
Chen, Zhilong; Hancheng Cao; Fengli Xu; Mengjie Cheng; Tao Wang; and Yong Li (2020). Understanding 
the role of intermediaries in online social e-commerce: an exploratory study of beidian. In: Proceed-
ings of the ACM on Human-Computer Interaction (PACMHCI), vol. 4, pp. 1–24.
Cheung, Gifford; and Jeff Huang (2011). Starcraft from the stands: understanding the game spectator. In: 
CHI’11: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Vancou-
ver BC Canada, 2011. New York: Association for Computing Machinery, pp. 763–772.
Choe, Hanwool (2019). Eating together multimodally: Collaborative eating in mukbang, a korean livestream 
of eating. Language in Society, vol. 48, pp. 171–208.
CINIC, China Internet Network Information Center (2020). The 46th china statistical report on internet 
development. Report. CINIC, December 2020. https://​www.​cnnic.​com.​cn/​IDR/​Repor​tDown​loads/​
202012/​P0202​01201​53002​34116​44.​pdf.
Coker, Brent (2020). Arousal enhances herding tendencies when decision making. Journal of Consumer 
Behaviour, vol. 19, pp. 229–239.
725

## TRANG 26

Y. Wang et al.
Comegys, Charles; Mika Hannula; and Jaaui Váisánen (2009). Effects of consumer trust and risk on online 
purchase decision-making: A comparison of finnish and United States students. International Journal 
of Management (IJM), vol. 26, pp. 295–308.
Corbin, Juliet; and Anselm Strauss (2014). Basics of qualitative research: Techniques and procedures for 
developing grounded theory. Thousand Oaks, California: Sage publications.
Cortese, Juliann; and Alan M. Rubin (2010). Uses and gratifications of television home shopping. Atlantic 
Journal of Communication (AJC), vol. 18, pp. 89–109.
Cunningham, Stuart; David Craig; and Junyi Lv (2019). China’s livestreaming industry: platforms, politics, 
and precarity. International Journal of Cultural Studies, vol. 22, pp. 719–736.
Darian, Jean C (1987). In-home shopping: are there consumer segments? Journal of Retailing, vol. 63, pp. 
163–186.
Day, Melody (2022). How tiktok created its own ecommerce platform. Technology News. Net Influencer, 
February 2022. https://​www.​netin​fluen​cer.​com/​how-​tiktok-​creat​ed-​its-​own-e-​comme​rce-​platf​orm/.
Dellarocas, Chrysanthos (2003). The digitization of word of mouth: Promise and challenges of online feed-
back mechanisms. Management Science (MS), vol. 49, pp. 1407–1424.
Dougherty, Audubon (2011). Live-streaming mobile video: production as civic engagement. In: Mobile-
HCI’11: Proceedings of the 13th international conference on human computer interaction with 
mobile devices and services, Stockholm Sweden, 30 August - 2 September 2011. New York: Associa-
tion for Computing Machinery, pp. 425–434.
Eastin, Matthew S.; Nancy H. Brinson; Alexandra Doorey; and Gary Wilcox (2016). Living in a big data 
world: Predicting mobile commerce activity through privacy concerns. Computers in Human Behav-
ior, vol. 58, pp. 214–220.
Engel, James F.; Martin R. Warshaw; Thomas C. Kinnear; and Bonnie B. Reece (2000). Promotional strat-
egy: an integrated marketing communication approach. Ann Arbor, Michigan: Pinnaflex Educational 
Resources Incorporated.
Erasmus, Alet C.; Elizabeth Boshoff; and GG. Rousseau (2001). Consumer decision-making models within the 
discipline of consumer science: a critical approach. Journal of Consumer Sciences (JCS), vol. 29, pp. 82–90.
Geng, Ruibin; Shichao Wang; Xi Chen; Danyang Song; and Jie Yu (2020). Content marketing in e-com-
merce platforms in the internet celebrity economy. Industrial Management & Data Systems, vol. 120, 
pp. 464–485.
Gibson, James J. (1977). The theory of affordances. Hilldale, USA, vol. 1, pp. 67–82.
Gorn, Gerald; Michel Tuan Pham; and Leo Yatming Sin (2001). When arousal influences ad evaluation and 
valence does not (and vice versa). Journal of consumer Psychology (JCP), vol. 11, pp. 43–55.
Hagtvedt, Henrik; and Vanessa M. Patrick (2008). Art infusion: the influence of visual art on the perception 
and evaluation of consumer products. Journal of Marketing Research (JMR), vol. 45, pp. 379–389.
Haimson, Oliver L.; and John C. Tang (2017). What makes live events engaging on facebook live, periscope, and 
snapchat. In: CHI’17: Proceedings of the 2017 CHI conference on human factors in computing systems, 
Denver Colorado USA, 2017. New York: Association for Computing Machinery, pp. 48–60.
Hamilton, William A.; Oliver Garretson; and Andruid Kerne (2014). Streaming on twitch: fostering partici-
patory communities of play within live mixed media. In: CHI’14: Proceedings of the SIGCHI confer-
ence on human factors in computing systems, Toronto Ontario Canada, 26 April 2014 - 1 May 2014. 
New York: Association for Computing Machinery, pp. 1315–1324.
Häubl, Gerald; and Valerie Trifts (2000). Consumer decision making in online shopping environments: the 
effects of interactive decision aids. Marketing Science, vol. 19, pp. 4–21.
Hawkins, Delbert; Roger J. Best; and Kenneth A. Coney (2009). Consumer behavior. New York: McGraw-
Hill Publishing.
Hennig-Thurau, Thorsten; Kevin P. Gwinner; Gianfranco Walsh; and Dwayne D. Gremler (2004). Electronic 
word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate themselves 
on the internet? Journal of Interactive Marketing, vol. 18, pp. 38–52.
Herabadi, Astrid G.; Bas Verplanken; and Ad Van Knippenberg (2009). Consumption experience of impulse 
buying in indonesia: Emotional arousal and hedonistic considerations. Asian Journal of Social Psychol-
ogy, vol. 12, pp. 20–31.
Hew, Khe Foon; and Noriko Hara (2007). Empirical study of motivators and barriers of teacher online 
knowledge sharing. Educational Technology Research and Development, vol. 55, p. 573.
Holtzman, Samuel (1988). Intelligent decision systems. Boston, Massachusetts: Addison-Wesley Longman 
Publishing Co., Inc.
Howard, Jonh A.; and Jagdish N. Sheth (2001). A theory of buyer behavior. Marketing: Critical Perspec-
tives on Business and Management, vol. 3, p. 81.
Hutchby, Ian (2001). Technologies, texts and affordances. Sociology, vol. 35, pp. 441–456.
726

## TRANG 27

How Live Streaming Changes Shopping Decisions in E‑commerce:…
Jarvenpaa, Sirkka L.; Noam Tractinsky; and Michael Vitale (2000). Consumer trust in an internet store. 
Information Technology and Management, vol. 1, pp. 45–71.
Kang, Yong-Soon; and Nancy M. Ridgway (1996). The importance of consumer market interactions as a form of 
social support for elderly consumers. Journal of Public Policy & Marketing (JPP&M), vol. 15, pp. 108–117.
Kasper, George M. (1996). A theory of decision support system design for user calibration. Information Sys-
tems Research (ISR), vol. 7, pp. 215–232.
Katawetawaraks, Chayapa; and Cheng Wang (2011). Online shopper behavior: Influences of online shopping 
decision. Asian Journal of Business Research (AJBR), vol. 1, pp. 66–75.
Keeling, Kathleen; Peter McGoldrick; and Susan Beatty (2010). Avatars as salespeople: Communication style, 
trust, and intentions. Journal of Business Research (JBR), vol. 63, pp. 793–800.
Koo, Dong-Mo; Jae-Jin Kim; and Sang-Hwan Lee (2008). Personal values as underlying motives of shopping 
online. Asia Pacific Journal of Marketing and Logistics (APJML), vol. 20, pp. 156–173.
Koyuncu, Cuneyt; and Gautam Bhattacharya (2004). The impacts of quickness, price, payment risk, and deliv-
ery issues on on-line shopping. The Journal of Socio-Economics, vol. 33, pp. 241–251.
Ku, Yi-Cheng; Yie-Fang Kao; and MingJiao Qin (2019). The effect of internet celebrity’s endorsement on 
consumer purchase intention. In: HCII 19’: International Conference on Human-Computer Interaction, 
Orlando, Florida, USA, 2019. New York: Springer, pp. 274–287.
Li, Wei (2020). Breakthrough of tv shopping with the new media. Research on Transmission Competence, vol. 
6, pp. 65–66.
Li, Yao; Yubo Kou; Je Seok Lee; and Alfred Kobsa (2018). Tell me before you stream me: Managing informa-
tion disclosure in video game live streaming. In: Proceedings of the ACM on Human-Computer Interac-
tion (PACMHCI), vol. 2, pp. 1–18.
Li, Jie; Xinning Gui; Yubo Kou; and Yukun Li (2019). Live streaming as co-performance: Dynamics between 
center and periphery in theatrical engagement. In: Proceedings of the ACM on Human-Computer Interac-
tion (PACMHCI), vol. 3, pp. 1–22.
Liao, Chechen; Pui-Lai To; Yun-Chi Wong; Prashant Palvia; and Mohammad Daneshvar Kakhki (2016). The 
impact of presentation mode and product type on online impulse buying decisions. Journal of Electronic 
Commerce Research (JECR), vol. 17, p. 153.
Lim, Heejin; and Alan J. Dubinsky (2004). Consumers’ perceptions of e-shopping characteristics: an expec-
tancy-value approach. Journal of Services Marketing (JSM), vol. 18, pp. 500–513.
Lim, Chae Mi; and Youn-Kyung Kim (2011). Older consumers’ tv home shopping: Loneliness, parasocial inter-
action, and perceived convenience. Psychology & Marketing, vol. 28, pp. 763–780.
Lin, Ching-Torng; Wei-Chiang Hong; Yi-Fun Chen; and Yucheng Dong (2010). Application of salesman-like 
recommendation system in 3g mobile phone online shopping decision support. Expert Systems with 
Applications, vol. 37, pp. 8065–8078.
Liu, Yihan (2021). Development from tv shopping to live-streaming. News-culture Construction, vol. 2, pp. 138–139.
Liu, Chung-Tzer; and Guo, Y.M. (2008). Validating the end-user computing satisfaction instrument for online 
shopping systems. Journal of Organizational and End User Computing (JOEUC), vol. 20, pp. 74–96.
Lottridge, Danielle; Frank Bentley; Matt Wheeler; Jason Lee; Janet Cheung; Katherine Ong; and Cristy Rowley 
(2017). Third-wave livestreaming: teens’ long form selfie. In: MobileHCI’17: Proceedings of the 19th 
International Conference on Human-Computer Interaction with Mobile Devices and Services, Vienna, 
Austria. 2017. New York: Association for Computing Machinery, pp. 1–12.
Lowry, Paul Benjamin; James Gaskin; and Gregory D. Moody (2015). Proposing the multi-motive information 
systems continuance model (misc) to better explain end-user system evaluations and continuance inten-
tions. Journal of the Association for Information Systems (JAIS), vol. 16, pp. 515–579.
Lu, Zhicong; Haijun Xia; Seongkook Heo; and Daniel Wigdor (2018). You watch, you give, and you engage: 
a study of live streaming practices in china. In: CHI’18: Proceedings of the 2018 CHI conference on 
human factors in computing systems, Montreal QC Canada, 2018. New York: Association for Computing 
Machinery, pp. 1–13.
Lu, Zhicong; Michelle Annett; and Daniel Wigdor (2019). Vicariously experiencing it all without going out-
side: a study of outdoor livestreaming in china. In: Proceedings of the ACM on Human-Computer Inter-
action (PACMHCI), vol. 3, pp. 1–28.
Ma, Xiaojuan; and Nan Cao (2017). Video-based evanescent, anonymous, asynchronous social interaction: 
Motivation and adaption to medium. In: CSCW’17: Proceedings of the 2017 ACM Conference on Com-
puter Supported Cooperative Work and Social Computing, Portland Oregon USA, 25 February 1 March 
2017. New York: Association for Computing Machinery, pp. 770–782.
Ma, Will W.K.; and Allan H.K. Yuen (2011). Understanding online knowledge sharing: an interpersonal rela-
tionship perspective. Computers & Education, vol. 56, pp. 210–219.
McLuhan, Marshall (1994). Understanding media: The extensions of man. Cambridge, Massachusetts: MIT Press.
727

## TRANG 28

Y. Wang et al.
Mehrabian, Albert (1996). Analysis of the big-five personality factors in terms of the pad temperament 
model. Australian Journal of Psychology, vol. 48, pp. 86–92.
Mehrabian, Albert; and James A. Russell (1974). An approach to environmental psychology. Cambridge, 
Massachusetts: The MIT Press.
MOFCOM, Ministry of Commerce of the People’s Republic of China. (2018). 2017 China tv shopping 
industry development report. Report. Ministry of Commerce of the Peoples Republic of China, May 
2018. http://​www.​gov.​cn/​xinwen/​2018-​06/​25/​53010​63/​images/​20180​62513​56142​11.​pdf.
Moser, Carol; Paul Resnick; and Sarita Schoenebeck (2017). Community commerce: Facilitating trust in 
mom-to-mom sale groups on facebook. In: CHI’17: Proceedings of the 2017 CHI Conference on 
Human Factors in Computing Systems, Denver Colorado USA, 2017. New York: Association for 
Computing Machinery, pp. 4344–4357.
Moser, Carol; Sarita Y. Schoenebeck; and Paul Resnick (2019). Impulse buying: Design practices and con-
sumer needs. In: CHI’19: Proceedings of the 2019 CHI Conference on Human Factors in Computing 
Systems, Glasgow Scotland UK, 2019. New York: Association for Computing Machinery, pp. 1–15.
Nagy, Peter; and Gina Neff (2015). Imagined affordance: Reconstructing a keyword for communication the-
ory. Social Media+ Society, vol. 1, pp. 1–9.
Nicosia, Francesco M.; and Robert N. Mayer (1976). Toward a sociology of consumption. Journal of Con-
sumer Research (JCR), vol. 3, pp. 65–75.
Park, Ji Hye; and Sharron J. Lennon (2004). Television apparel shopping: Impulse buying and parasocial 
interaction. Clothing and Textiles Research Journal (CTRJ), vol. 22, pp. 135–144.
Pazgal, Amit; and David Soberman (2008). Behavior-based discrimination: is it a winning play, and if so, 
when? Marketing Science (MS), vol. 27, pp. 977–994.
Peng, Lifang; Qinyu Liao; Xiaorong Wang; and Xuanfang He (2016). Factors affecting female user informa-
tion adoption: an empirical investigation on fashion shopping guide websites. Electronic Commerce 
Research, vol. 16, pp. 145–169.
Peukert, Christian; Jella Pfeiffer; Martin Meißner; Thies Pfeiffer; and Christof Weinhardt (2019). Shop-
ping in virtual reality stores: the influence of immersion on system adoption. Journal of Management 
Information Systems (JMIS), vol. 36, pp. 755–788.
PPostigo, Hector (2016). The socio-technical architecture of digital labor: Converting play into youtube 
money. New Media & Society, vol. 18, pp. 332–349.
Prasad, Ch JS; and A.R. Aryasri (2009). Determinants of shopper behaviour in e-tailing: an empirical analy-
sis. Paradigm, vol. 13, pp. 73–83.
Qin, Xuebing; and Zhibin Jiang (2019). The impact of ai on the advertising process: the chinese experience. 
Journal of Advertising, vol. 48, pp. 338–346.
Salam, Al F.; Lakshmi Iyer; Prashant Palvia; and Rahul Singh (2005). Trust in e-commerce. Communica-
tions of the ACM, vol. 48, pp. 72–77.
Sevitt, David; and Alexandra Samuel (2013). How pinterest puts people in stores. Harvard Business Review, 
vol. 91, pp. 26–27.
Singh, Mohini (2002). E-services and their role in b2c e-commerce. Managing Service Quality: An Interna-
tional Journal, vol. 12, pp. 434–446.
Sjöblom, Max; and Juho Hamari (2017). Why do people watch others play video games? an empirical study 
on the motivations of twitch users. Computers in Human Behavior, vol. 75, pp. 985–996.
Stephens, Debra Lynn; Ronald Paul Hill; and Karyn Bergman (1996). Enhancing the consumer-product 
relationship: Lessons from the qvc home shopping channel. Journal of Business Research (JBR), vol. 
37, pp. 193–200.
Sutanonpaiboon, Janejira; and Ayman Abuhamdieh (2008). Factors influencing trust in online consumer-to-
consumer (c2c) transactions. Journal of Internet Commerce, vol. 7, pp. 203–219.
Szymkowiak, Andrzej; Piotr Gaczek; Kishokanth Jeganathan; and Piotr Kulawik (2021). The impact of 
emotions on shopping behavior during epidemic. what a business can do to protect customers. Jour-
nal of Consumer Behaviour, vol. 20, pp. 48–60.
Taber, Lee; Leya Breanna Baltaxe-Admony; and Kevin Weatherwax (2019). What makes a live stream com-
panion? animation, beats, and parasocial relationships. Interactions, vol. 27, pp. 52–57.
Tang, John C.; Gina Venolia; and Kori M. Inkpen (2016). Meerkat and periscope: I stream, you stream, apps 
stream for live streams. In: CHI’16: Proceedings of the 2016 CHI Conference on Human Factors in 
Computing Systems, San Jose California USA, 2016. New York: Association for Computing Machin-
ery, pp. 4770–4780.
Thomas, Richard K. (2005). Marketing health services. Washington, D.C.: Health Administration Press. 
Arlington: AUPHA Press.
728

## TRANG 29

How Live Streaming Changes Shopping Decisions in E‑commerce:…
Van der Heijden, Hans; Tibert Verhagen; and Marcel Creemers (2003). Understanding online purchase intentions: 
contributions from technology and trust perspectives. European Journal of Information Systems, vol. 12, pp. 
41–48.
Wang, Weiquan; and Izak Benbasat (2008). Attributions of trust in decision support technologies: a study of rec-
ommendation agents for e-commerce. Journal of Management Information Systems (JMIS), vol. 24, pp. 
249–273.
Wang, Cheng Lu; Yue Zhang; Li Richard Ye; and Dat-Dao Nguyen (2005). Subscription to fee-based online 
services: What makes consumer pay for online content? Journal of Electronic Commerce Research 
(JECR), vol. 6, p. 304.
Wang, Dennis; Yi-Chieh Lee; and Wai-Tat Fu (2019). “I love the feeling of being on stage, but i become greedy” 
exploring the impact of monetary incentives on live streamers’ social interactions and streaming content. In: 
Proceedings of the ACM on Human-Computer Interaction (PACMHCI), vol. 3, pp. 1–24.
Wei, He (2020). Livestream selling goes global. News. China Daily, August 2020. https://​www.​china​daily​hk.​
com/​artic​le/​140150.
Wirtz, Jochen; Anna S. Mattila; and Rachel L.P. Tan (2007). The role of arousal congruency in influencing con-
sumers’ satisfaction evaluations and in-store behaviors. International Journal of Service Industry Man-
agement, vol. 18, pp. 6–24.
Wohn, Donghee Yvette; Guo Freeman; and Caitlin McLaughlin (2018). Chi’18: Explaining viewers’ emotional, 
instrumental, and financial support provision for live streamers. In: Proceedings of the 2018 CHI confer-
ence on human factors in computing systems, Montreal QC Canada, 2018. New York: Association for 
Computing Machinery, pp. 1–13.
Wongkitrungrueng, Apiradee; and Nuttapol Assarut (2018). The role of live streaming in building consumer 
trust and engagement with social commerce sellers. Journal of Business Research (JBR), vol. 117, pp. 
543–556.
Yi, Kejie (2020). Top kuaishou live streamer xinba caught selling fake products. News. China Marketing 
Insights, December 2020. https://​china​mktgi​nsigh​ts.​com/​top-​kuais​hou-​live-​strea​mer-​xinba-​caught-​selli​
ng-​fake-​produ​cts/.
Zhong, Raymond (2020). Why does walmart want tiktok? looking to china may explain. Article. The New York 
Times, August 2020. https://​www.​nytim​es.​com/​2020/​08/​28/​techn​ology/​tiktok-​walma​rt-​ecomm​erce.​html.
Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published 
maps and institutional affiliations.
729

