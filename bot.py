from selenium import webdriver
import time
import mysql.connector
import datetime


from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Windows/chromedriver.exe')

conexion = mysql.connector.connect(host='localhost',database='aztecaseo',user='root',password='')
cursor = conexion.cursor()
#pagina para ingresar
# xpaht boton submit recaptcha //*[@id="recaptcha_submit"]
#xpaht boton on page seo Checker /html/body/div[2]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/a[4]
#enlace botn on page seo Checker https://www.semrush.com/on-page-seo-checker/2234267/overview/

driver.get("https://www.semrush.com/")
#username y password pasar a diccionanrio segun cuenta pasar a diccionario
user_name = "info@quickcleanchicago.com"
password = "newpp2020bx"
#login user y pass
elem = driver.find_element_by_xpath("//*[@data-test='auth-popup__btn-login']").click()
elem = driver.find_element_by_xpath("//*[@data-test='login-page__input-email']")
elem.send_keys(user_name)
elem = driver.find_element_by_xpath("//*[@data-test='login-page__input-password']")
elem.send_keys(password)
elem = driver.find_element_by_xpath("//*[@data-test='login-page__btn-login']").click()
time.sleep(2)
#elem = driver.find_element_by_xpath("//*[@data-test='base-popup-close']").click()
urlcambiar= "2234267"
driver.get("https://www.semrush.com/tracking/landscape/"+urlcambiar+".html")
#elem = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/div[1]/div[6]/div/div[1]/div[2]/table/tbody/tr[3]/td[1]/a").click()
elem = driver.find_element_by_xpath('//*[@id="root-content"]/div[3]/div/div[2]/div[5]/ul/li[2]/a').click()
time.sleep(3)

elem = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[2]/div/a')
pos = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[5]/span/div/span')
url_track = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[11]/div/a[1]')
postr = pos.text
element = elem.text
url_trackt = url_track.text
element_attribute_value = elem.get_attribute('value')
com1 = "'"
com2 = "'"

tbodall = driver.find_elements_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr')

canti = len(tbodall)
for i in range(1,canti):
    vari = str(i)
    var1 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[2]/div/a')
    var2 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[5]/span/div/span')
    var3 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[11]/div/a[1]')
    print("Keyword: "+var1.text+" Posicion: "+var2.text +" URL: "+var3.text)
    var1t = var1.text
    var2t = var2.text
    var3t = var3.text
    query1 = "SELECT * FROM positiontrak WHERE positiontrak.keyphrase ="+com1+var1t+com2
    cursed = conexion.cursor(buffered=True)
    cursed.execute(query1)
    rowscount = cursed.rowcount
    if rowscount == 1:
        varhome = "https://quickcleanchicago.com/"
        if var3t == varhome:
            query = "update positiontrak set positiontrak.keyphrase="+com1+var1t+com2+",positiontrak.pos="+var2t+" where positiontrak.keyphrase="+com1+var1t+com2
            cursor.execute(query)
            conexion.commit()
            print("Cambio con exito Sin Url")
        else:
            query = "update positiontrak set positiontrak.keyphrase="+com1+var1t+com2+",positiontrak.pos="+var2t+" ,positiontrak.url="+com1+var3t+com2+" where positiontrak.keyphrase="+com1+var1t+com2
            cursor.execute(query)
            conexion.commit()
            print("Cambio con exito")
    else:
        query = "INSERT INTO positiontrak (id_track, id_campana, keyphrase, pos, url) VALUES (%s, %s, %s,%s, %s)"
        val = ("NULL",6,var1t,var2t,var3t)
        cursor.execute(query,val)
        conexion.commit()
        print("Frase clave agregada con exito")

time.sleep(1)



driver.get("https://www.semrush.com/on-page-seo-checker/2234267/scores/all/")
time.sleep(5)
tdbodytask = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr')
cantitask = len(tdbodytask)

print("cantitask: "+ str(len(tdbodytask)))

aux = 1
while aux <= cantitask:
    query1 = "SELECT * FROM positiontrak WHERE positiontrak.keyphrase ="+com1+var1t+com2
    cursed = conexion.cursor(buffered=True)
    cursed.execute(query1)


    varitext = str(aux)
    var1task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr['+varitext+']/td[3]/div/span')
    var2task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr['+varitext+']/td[4]/div/div/div/a/span/span')
    varcrows = var2task.text
    aux = aux + 1


    fetcrows = "SELECT * FROM positiontrak WHERE positiontrak.keyphrase ="+com1+varcrows+com2
    cursed = conexion.cursor(buffered=True)
    cursed.execute(fetcrows)
    records = cursed.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
        print("id_track: "+ str(row[0]))
        print("id_campana: "+ str(row[1]))
        print("keyphrase: "+ str(row[2]))
        print("pos: "+ str(row[3]))
        print("url: "+ str(row[4]))
        print("\n")
        id_trakbd = str(row[0])
        insertoorders = "INSERT INTO ordenes(id_orden, frase_objetiva, tipo_orden, sin1, sin2, sin3, sin4, id_camp, fechaini, fechafinal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = ("null",id_trakbd,1,"sin","sin","sin","sin",6,"2020-01-07","2020-01-07")
        cursor.execute(insertoorders,val)
        conexion.commit()
        print("Frase clave agregada con exito")

    cursed.close()
    ciclo = 1
    while ciclo <= cantitask:
        ciclotext = str(ciclo)
        ideas = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr[1]/td[6]/div/button').click()
        time.sleep(4)
        strategy = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/ul/li[1]/div[2]')
        strategylen = str(len(strategy))
        print("esto es algo> "+strategylen)
        strategytext = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/ul/li[1]/div[2]/span['+strategylen+']')

        #print(strategytext.text)


        ciclo = ciclo + 1


    print ("Valor actual de la variable : " + var1task.text + "Frase: " + var2task.text)
print ("fin del script")
