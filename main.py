from logger import fileio
from logger import logger
from twitter import authenticator


def main():
    def generate_logger(data_dir):
        auth = authenticator.Authenticator("./twitter_credentials.json")
        api = auth.authenticate()
        io = fileio.CSVHandler(data_dir)
        return logger.Logger(api, io)

    # simple: 1,500,000 tweets ~ 0.7GB ~ 24 hours
    # dynamics: 2,500 tweets ~ 0.15GB ~ 24 hours
    # logger_ = generate_logger("../data/covid-19/20200508_simple")
    # logger_.track_dynamics(0.5, 1500000 * 30, additional_q="\"コロナ\"",)

    # from twitter import error
    # import tweepy
    # auth = authenticator.Authenticator("./twitter_credentials.json")
    # api = auth.authenticate()
    io = fileio.CSVHandler("../data/covid-19/20200508_simple")
    tweets_df = io.read_tweets()
    # ids = list(tweets_df.index)
    # deleted_ids = set()
    # for i in range(0, 10000, 100):
    #     j = i + 100
    #     ids_ = set(ids[i:j])
    #     try:
    #         tweets = api.statuses_lookup(id_=ids_, tweet_mode="extended")
    #     except (error.TotalRateLimitError, tweepy.TweepError) as e:
    #         print(e)
    #         print(ids_)
    #     else:
    #         got_ids = {str(tweet.id) for tweet in tweets}
    #         deleted_ids |= ids_ - got_ids
    # print(deleted_ids)
    deleted_ids = {'1258775570218811394', '1258775101299781632', '1258774175482703874', '1258774155958214658', '1258774704715780098', '1258773866509332481', '1258775083285229569', '1258775788620378112', '1258773995110817794', '1258773944531738625', '1258774103038652419', '1258775763530076161', '1258774652513484801', '1258775597863428096', '1258775024212688897', '1258774282743644161', '1258774089663016967', '1258775369508773894', '1258774527485423616', '1258774961319079937', '1258774636776448000', '1258774803382595590', '1258774946274131970', '1258775242924625921', '1258774416466472962', '1258775442116337664', '1258773648292237315', '1258773676192759808', '1258775201170354179', '1258774102870863872', '1258774427317100547', '1258774901587996672', '1258773946675027974', '1258775709889118208', '1258776006036295680', '1258775899891052545', '1258774089642110981', '1258773874528796672', '1258775181369069569', '1258774504345493504', '1258774244596408320', '1258774600680214528', '1258773651236646913', '1258774564261093376', '1258773884825812992', '1258773666369691649', '1258775153799913474', '1258775317524516864', '1258775321207160832', '1258774118029119490', '1258776127977385985', '1258776059090104321', '1258773891339571200', '1258774215953506306', '1258775431127302144', '1258775832677330946', '1258775086288392192', '1258775970665783297', '1258773800289624066', '1258776082926338048', '1258773874893680641', '1258775817187807241', '1258773766265376768', '1258774030468870145', '1258774013393829889', '1258774674474856448', '1258775019334721536', '1258774933842223105', '1258775718420340737', '1258773715719864320', '1258773664389971968', '1258776037753622529', '1258774878187995138', '1258775128155885568', '1258775472684457985', '1258774478940631043', '1258775049919623168', '1258775925346365441', '1258776174580297729', '1258775246338879488', '1258775990118973440', '1258776078950100993', '1258774704141172736', '1258774074244755457', '1258773764591906816', '1258773850289893377', '1258774873876295681', '1258775498341007360', '1258775736040611840', '1258774958353891328', '1258775874037444615', '1258774402050560000', '1258775205108801536', '1258775528628121601', '1258774817345466368', '1258774701901361154', '1258775055653195778', '1258774604727726083', '1258775403960782848', '1258775902336348161', '1258774007358173190', '1258774153013817344', '1258775862058483713', '1258774313978621954', '1258774036558970880', '1258775645888237571', '1258773720895680512', '1258773771181154305', '1258774642635894784', '1258774744901447682', '1258774855421321217', '1258773789959045120', '1258775547053654016', '1258776159254220801', '1258776034998022145', '1258774687636582400', '1258775331252494339', '1258775864583454720', '1258775866022084608', '1258775365461262336', '1258774062223855616', '1258774174987776001', '1258773903742169088', '1258775125224112128', '1258774025905467393', '1258774163688316930', '1258774353077923840', '1258773830929014786', '1258773664272506882', '1258776069345177601', '1258775480250982400', '1258773795138965504', '1258775090071654400', '1258774249721888778', '1258775366220439554', '1258774452134793216', '1258775409597968387', '1258774532321538049', '1258774952687226882', '1258775517559271425', '1258774459760078849', '1258774361659465730', '1258776166170628097', '1258774254864105472', '1258775239640576001', '1258775393525329920', '1258774537971175429', '1258775735382102017', '1258775671108587523', '1258774924170166272', '1258775252357615622', '1258775201312956417', '1258773991843487744', '1258775921328181248', '1258774376645681153', '1258773949661372417', '1258774514856427520', '1258776074684526593', '1258773748414443521', '1258775687931949059', '1258775941666365440', '1258773826382356480', '1258775363544473602', '1258775057670696967', '1258775044731179013', '1258775796442820612', '1258774550466097152', '1258773829301620737', '1258773807000518659', '1258774288808595456', '1258774586016989184', '1258775486844424194', '1258774291186769920', '1258775901212258304', '1258775730386690048', '1258775172862971904', '1258773919068086272', '1258775139379933185', '1258774486599385090', '1258775326454235137', '1258773726822195200', '1258775566091599873', '1258774060315492352', '1258775033712787457', '1258774540512985088', '1258775620663689218', '1258776005407207425', '1258776146432294912', '1258775203330486273', '1258776154816655360', '1258774584196657153', '1258774619927924737', '1258775441671720960', '1258774270026510337', '1258775241842520064', '1258773718450368515', '1258775428275286022', '1258775162201075712', '1258774570963578881', '1258773713656279040', '1258774035187421185', '1258773710443446273', '1258775066117980160', '1258773724200792065', '1258775932245913600', '1258774562872811520', '1258774647299952640', '1258774924556042242', '1258775049789534209', '1258775135961505802', '1258776009152708608', '1258774095690268673', '1258775168677105665', '1258775651407917056', '1258775402606063616', '1258774745627017216', '1258775015454937091', '1258774486762967040', '1258774262669651970', '1258775207826698240', '1258774716497551360', '1258776033618063360', '1258775650527141888', '1258776102039777286', '1258776156788060162', '1258775975917006850', '1258774732217782272', '1258774758994276352', '1258775695968178177', '1258775596881965056', '1258773644777406469', '1258775870518571016', '1258773745377796096', '1258773721096962050', '1258774294496079872', '1258776005730119681', '1258774023091023872', '1258775002339405826', '1258774566962266113', '1258775406934585345', '1258775945168617472', '1258775104772665344', '1258774825981468672', '1258773667988729857', '1258773779125133313', '1258775622865661953', '1258775684949790720', '1258774181384081408', '1258773674653446147', '1258774273700753408', '1258773821445648385', '1258775294955020288', '1258774730183565313', '1258774702463619077', '1258774734084337664', '1258773975628255233', '1258774088337637377', '1258774315924729861', '1258775992807514112', '1258774914728775686', '1258775044282388480', '1258774021639827457', '1258774799402143746', '1258775452207861761', '1258775745049972736', '1258773643313573890', '1258773666063454209', '1258775817854660609', '1258774409990430720', '1258775200566407168', '1258776067097063425', '1258774059837341696', '1258775376395857920', '1258773953289416711', '1258774487383719938', '1258774834814652416', '1258773916182441985', '1258774444278857733', '1258774540424843264', '1258773867536908292', '1258774077159792640', '1258773710510583809', '1258773887745024000', '1258774094796820480', '1258776060864327681', '1258775402987716609', '1258776073426178048', '1258775396729778176', '1258774406857256963', '1258775018479079424', '1258774810936500224', '1258773971798908929', '1258774398976225281', '1258775329629331457', '1258775134095077376', '1258774961331646467', '1258774710583607296', '1258774291555823616', '1258773918837469184', '1258775991108820992', '1258775543899541511', '1258774327677186050', '1258774119186706432', '1258774479590711301', '1258773970800668672', '1258774805488132096', '1258773961376059393', '1258774747782897664', '1258776121836883969', '1258774155832352770', '1258774299722125312', '1258773921408544768', '1258774438343880705', '1258775446667227137', '1258774463824322561', '1258775466208423937', '1258774140560920577', '1258774528185864192', '1258775670953439232', '1258775874444292101', '1258775882107252739', '1258774267023392768', '1258774489204051969', '1258774092246728704', '1258775141057613832', '1258775696307937287', '1258774040891686912', '1258774077809909761', '1258776013657354242', '1258773994305515520', '1258775475075182594', '1258774085313548290', '1258775010543464448', '1258775958087102470', '1258775361984147456', '1258773923379810304', '1258775924234809346', '1258773979432488960', '1258775724288167936', '1258774764170047489', '1258775093938806785', '1258774351123345408', '1258773749286842371', '1258775244967272453', '1258773682266075136', '1258773761710489601', '1258775480871776256', '1258775718340685824', '1258775651252760576', '1258775668076064774', '1258775447866757121', '1258774121183240193', '1258775202885808128', '1258775098481192960', '1258775095008301056', '1258775225761558533', '1258776017050546176', '1258774403627671556', '1258773754357837825', '1258773732450947073', '1258774160903270400', '1258773817108783110', '1258774029005029376', '1258774485815095296', '1258774362057924609', '1258774552525434881', '1258775666700349442', '1258773927414792192', '1258775224981442560', '1258774211314634753', '1258774364918444033', '1258774412934803459', '1258775241490223104', '1258773813254164481', '1258775015207534594', '1258775860150059009', '1258775935026790400', '1258774405196341248', '1258773873039794177', '1258774800412991488', '1258774911029407745', '1258773672925392896', '1258774595898757120', '1258775470545354752', '1258775721943547904', '1258774639712456704', '1258776169022808067', '1258774804234039299', '1258775654947934209', '1258774088006332416', '1258775025743589377', '1258774731471253504', '1258774871976243200', '1258775836838129665', '1258774427384156162', '1258774674747490304', '1258774737666191361', '1258775788012232705', '1258774543377678337', '1258774521512771584', '1258773996822134785', '1258775302194360320', '1258775178747625472', '1258774071442984960', '1258774302884691968', '1258775925509873664', '1258775708257546240', '1258773749693743105', '1258774503103971329', '1258774391938093056', '1258774490546229250', '1258774951613435905', '1258775979557707778', '1258775695066464258', '1258774643080482816', '1258774612231372803', '1258773743242903554', '1258774490470727681', '1258776166451736577', '1258773952710586368', '1258774250434912256', '1258774414901952513', '1258774649980063745', '1258774191135834112', '1258775893616414720', '1258775236482224129', '1258775693103558656', '1258776047077613569', '1258775785009057793', '1258774654287671297', '1258774335386292224', '1258774110273892353', '1258774251542175745', '1258773963271888896', '1258775368418291714', '1258774479708119040', '1258776021446189056', '1258774925508132864', '1258775493328859137', '1258775660115288067', '1258775154919763970', '1258773743012155392', '1258774485680812033', '1258773858724638726', '1258775560055959552', '1258774460913475584', '1258774456211697664', '1258774550075936768', '1258774714236854273', '1258776116292018176', '1258774860257357826', '1258775531304058885', '1258774517779841024', '1258774691520471040', '1258774169774198784', '1258775467215052800', '1258774860064419841', '1258774758511935490', '1258775263191560192', '1258774040937824256', '1258773795197685760', '1258773726792802305', '1258774074664214531', '1258775268912594944', '1258775133302358018', '1258775484944400389', '1258775902592229376', '1258775097306800130', '1258775801454968832', '1258775583556726784', '1258776173191901184', '1258774701834244096', '1258774516257353734', '1258773820644528129', '1258774916465168384', '1258774831169810440', '1258775255608201216', '1258773901489762304', '1258773794346299393', '1258773678851911682', '1258775179825537024', '1258774630690480128', '1258773693494222849', '1258774489698988033', '1258775063056150530', '1258775730978091008', '1258775758857625600', '1258775961090371584', '1258775082307997698', '1258773675278397440', '1258773978967011329', '1258775613952802819', '1258775259177615360', '1258775997710659588', '1258773954736476161', '1258774075578540038', '1258775003245342720', '1258774785351286784', '1258774069895237637', '1258775992618737670', '1258773904463589376', '1258773811253538817', '1258775148452175872', '1258776134998618112', '1258774832994414593', '1258776164929167360', '1258774005135183872', '1258775833927278593', '1258773861488709634', '1258774523119194112', '1258775376244826117', '1258774822714085377', '1258774348975845379', '1258776084675325953', '1258774525304434691', '1258775025491931136', '1258775583393116166', '1258774988238118913', '1258775559724691456', '1258773879553536006', '1258775910850760704', '1258775235769233409', '1258775680193409026', '1258774133736800258', '1258775604851118082', '1258775259601240070', '1258774704682221568', '1258775147667812354', '1258775211484123136', '1258775045863698432', '1258774799939072002', '1258774655583744000', '1258774656917491712', '1258774769328984064', '1258775730306990080', '1258775981222793216', '1258775510185697283', '1258774089537216514', '1258776012554301440', '1258775309588914176', '1258776174706098182', '1258774391866789888', '1258774915085295617', '1258775141720354817', '1258776135489294336', '1258774927127109642', '1258775598589042690', '1258776137947217923', '1258774968621383681', '1258774406056128513', '1258774046176456710', '1258774115378327554', '1258774951156277248', '1258774089289748483', '1258774966301908992', '1258773884125364225', '1258775683209195520', '1258776159459741697', '1258775194560126978', '1258775121210167296', '1258773683209822214', '1258773885803085824', '1258774961390415872', '1258774186517909504', '1258775371111006211', '1258774539317596161', '1258775904777457664', '1258776038277955584', '1258774392948965382', '1258774981619539968', '1258774980315103232', '1258774734608625665', '1258774296261832704', '1258775378618806272', '1258773683855736836', '1258773966207897601', '1258774838212038657', '1258775769314033665', '1258774322362998784', '1258774211104915457', '1258774414243446785', '1258775919017123841', '1258775651982569473', '1258774433046528000', '1258773941893513216', '1258775735017197568', '1258775467273814022', '1258775245613236226', '1258775687613132802', '1258775660505337856', '1258775314664046592', '1258774837507403778', '1258774203450310658', '1258775838914252800', '1258776077490520064', '1258774795161726982', '1258774684880867328', '1258774053952778240', '1258774389136297989', '1258773681037168640', '1258774999126675456', '1258774467464970240', '1258774200266846208', '1258774986686251013', '1258775667237203969', '1258773753032368135', '1258774879559512068', '1258773927377027072', '1258775383597395968', '1258773662045372418', '1258774526151684096', '1258775163459395584', '1258776090589315072', '1258774653281038337', '1258774328033697792', '1258774978347954177', '1258775672417206277', '1258775985303908353', '1258774018821287936', '1258775497300824065', '1258774261499457536', '1258775894304288771', '1258773966354739202', '1258774631218987009', '1258773759755878400', '1258774192654188545', '1258775474940960770', '1258775397119832065', '1258773836968820738', '1258774630552072192', '1258775904555134976', '1258775416950546437', '1258775454627926016', '1258775174024843265'}
    for id_, df in tweets_df.groupby("id", observed=True):
        if id_ in deleted_ids:
            print(df.iloc[0]["full_text"])


if __name__ == "__main__":
    main()