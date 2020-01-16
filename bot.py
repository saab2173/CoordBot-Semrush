# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import mysql.connector
from datetime import datetime
from datetime import timedelta
from selenium.common.exceptions import NoSuchElementException




from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Windows/chromedriver.exe')
conexion = mysql.connector.connect(host='localhost',database='aztecaseo',user='root',password='')
cursor = conexion.cursor()


time.sleep(2)
#pagina para ingresar (id)

id_campana = "6"
driver.get("https://www.semrush.com/login/")
datoscamp = "SELECT * FROM campana WHERE id_campana ="+id_campana
cursed = conexion.cursor(buffered=True)
cursed.execute(datoscamp)
records = cursed.fetchall()
for row in records:
    conexion.commit()
    #username y password
    user_name = str(row[24])
    password = str(row[25])
    #login user y pass
    elem = driver.find_element_by_xpath("//*[@data-test='login-page__input-email']")
    elem.send_keys(user_name)
    elem = driver.find_element_by_xpath("//*[@data-test='login-page__input-password']")
    elem.send_keys(password)
    elem = driver.find_element_by_xpath("//*[@data-test='login-page__btn-login']").click()
    time.sleep(2)
    urlcambiar= str(row[26])
    driver.get("https://www.semrush.com/tracking/overview/"+urlcambiar+".html")

cursed.close()
# time.sleep(1)
# elem = driver.find_element_by_xpath('//*[@id="root-content"]/div[3]/div/div[2]/div[5]/ul/li[2]/a').click()
time.sleep(3)
elem = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[2]/div/a')
pos = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[5]/span/div/span')
url_track = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[11]/div/a[1]')
postr = pos.text
element = elem.text
url_trackt = url_track.text
element_attribute_value = elem.get_attribute('value')
com1 = "'"

tbodall = driver.find_elements_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr')

canti = len(tbodall)
for i in range(1,canti+1):
    vari = str(i)
    var1 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[2]/div/a')
    var2 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/div/div/table/tbody/tr['+vari+']/td[5]')
    if( var2.text.isdigit()):
        var_exit = "Es un numero"
    else:
        var3 = driver.find_elements_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[11]/div/a')
        var3_len = len(var3)
        if var3_len > 0:
            var_3 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[11]/div/a[2]')
        var1t = var1.text
        var2t = "100"
        var3t = var_3.get_attribute('href')
        query1 = "SELECT * FROM positiontrak WHERE positiontrak.keyphrase ="+com1+var1t+com1
        cursed = conexion.cursor(buffered=True)
        cursed.execute(query1)
        rowscount = cursed.rowcount
        if rowscount == 1:
            varhome = "https://quickcleanchicago.com/"
            if var3t == varhome:
                query = "update positiontrak set positiontrak.keyphrase="+com1+var1t+com1+",positiontrak.pos="+var2t+" where positiontrak.keyphrase="+com1+var1t+com1
                cursor.execute(query)
                conexion.commit()
                print("Cambio con exito Sin Url")
            else:
                query = "update positiontrak set positiontrak.id_campana="+com1+id_campana+com1+", positiontrak.keyphrase="+com1+var1t+com1+",positiontrak.pos="+var2t+" ,positiontrak.url="+com1+var3t+com1+" where positiontrak.keyphrase="+com1+var1t+com1
                cursor.execute(query)
                conexion.commit()
    
                print("Cambio con exito")
        else:
            query = "INSERT INTO positiontrak (id_campana, keyphrase, pos, url) VALUES (%s, %s, %s,%s)"
            val = (id_campana,var1t,var2t,var3t)
            cursor.execute(query,val)
            conexion.commit()
            print("Frase clave agregada con exito")
    
    var3 = driver.find_elements_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[11]/div/a')
    var3_len = len(var3)
    if var3_len > 0:
        var_3 = driver.find_element_by_xpath('//*[@id="react-page-container"]/div/div[2]/div[4]/div[2]/div[3]/div/div/div[1]/div/div/div/table/tbody/tr['+vari+']/td[11]/div/a[2]')
        var1t = var1.text
        var2t = var2.text
        var3t = var_3.get_attribute('href')
        query1 = "SELECT * FROM positiontrak WHERE positiontrak.keyphrase ="+com1+var1t+com1
        cursed = conexion.cursor(buffered=True)
        cursed.execute(query1)
        rowscount = cursed.rowcount
        if rowscount == 1:
            varhome = "https://quickcleanchicago.com/"
            if var3t == varhome:
                query = "update positiontrak set positiontrak.keyphrase="+com1+var1t+com1+",positiontrak.pos="+var2t+" where positiontrak.keyphrase="+com1+var1t+com1
                cursor.execute(query)
                conexion.commit()
                print("Cambio con exito Sin Url")
            else:
                query = "update positiontrak set positiontrak.id_campana="+com1+id_campana+com1+", positiontrak.keyphrase="+com1+var1t+com1+",positiontrak.pos="+var2t+" ,positiontrak.url="+com1+var3t+com1+" where positiontrak.keyphrase="+com1+var1t+com1
                cursor.execute(query)
                conexion.commit()
    
                print("Cambio con exito")
        else:
            query = "INSERT INTO positiontrak (id_campana, keyphrase, pos, url) VALUES (%s, %s, %s,%s)"
            val = (id_campana,var1t,var2t,var3t)
            cursor.execute(query,val)
            conexion.commit()
            print("Frase clave agregada con exito")
time.sleep(1)



driver.get("https://www.semrush.com/on-page-seo-checker/"+urlcambiar+"/scores/all/")
time.sleep(5)
tdbodytask = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr')
cantitask = len(tdbodytask)

print("Cantidad de tareas: "+ str(len(tdbodytask)))

for i in range(1,cantitask+1):
    task_i = str(i)
    urltask = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr['+task_i+']/td[3]/div/span')
    var2task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr['+task_i+']/td[4]/div/div/div/a/span/span')
    
    print("Frase Objetiva: "+var2task.text)
    print("Url de la Tarea: "+urltask.text)
    ulr_insert = urltask.text
    
    ordenes_query = "SELECT * FROM ordenes WHERE url_diff ="+com1+urltask.text+com1
    cursed = conexion.cursor(buffered=True)
    cursed.execute(ordenes_query)
    ordenes_rows = cursed.fetchall()
    ordenes_rows_len = len(ordenes_rows)
    if ordenes_rows_len == 1:
        for row_o in ordenes_rows:
            id_ordenes = str(row_o[0])
            query_errors = "SELECT * FROM errores WHERE id_tarea ="+com1+id_ordenes+com1
            cursed = conexion.cursor(buffered=True)
            cursed.execute(query_errors)
            errors_rows = cursed.fetchall()
            errors_rows_len = len(errors_rows)
            if errors_rows_len == 1:
                for row_e in errors_rows:
                    id_task_e = str(row_e[1])
                    errors_update = "UPDATE errores SET id_tarea="+com1+id_task_e+"WHERE id_tarea ="+com1+id_task_e+com1
                    print("Update de Errores: "+ id_task_e)
            else:
                
                errors_insert = "INSERT INTO errores(id_tarea, titulo_h1, contenido_titulo_h1, sub_1, texto_sub_1, sub_2, texto_sub_2, sub_3, texto_sub_3, sub_4, texto_sub_4, meta_tag, title_tag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (id_ordenes,"vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio","vacio",)
                cursed = conexion.cursor(buffered=True)
                cursed.execute(errors_insert,val)
                conexion.commit()
                print("Insert de Errores: " + id_ordenes)
                print("\n")
                
        url_bd = str(row[8])
        date_ini_fin = datetime.now()
        formatted_date = date_ini_fin.strftime('%Y-%m-%d')
        string_date = str(formatted_date)
        seven_days = datetime.now() + timedelta(days=7)
        print("Fecha de inicio de Orden: "+string_date)
        seven_days_formatted = str(seven_days.strftime('%Y-%m-%d'))
        print("Fecha de finalizacion de Orden: "+seven_days_formatted)
        ordenes_query_update = "UPDATE ordenes SET ordenes.fechaini="+com1+string_date+com1+",ordenes.fechafinal="+com1+seven_days_formatted+com1+" WHERE ordenes.url_diff ="+com1+ulr_insert+com1
        cursed = conexion.cursor(buffered=True)
    	cursed.execute(ordenes_query_update)
     	conexion.commit()
        print("Update de orden")
        print("\n")
            
    else:
        fetcrows = "SELECT * FROM positiontrak WHERE positiontrak.keyphrase ="+com1+var2task.text+com1
        cursed = conexion.cursor(buffered=True)
        cursed.execute(fetcrows)
        records = cursed.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            id_trakbd = str(row[0])
            ordenes_query_insert ="INSERT INTO ordenes(frase_objetiva, tipo_orden, sin1, sin2, sin3, sin4, id_camp, url_diff, fechaini, fechafinal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id_trakbd,1,"sin","sin","sin","sin",id_campana,ulr_insert,"2020-01-07","2020-01-07")
            cursed = conexion.cursor(buffered=True)
            cursed.execute(ordenes_query_insert,val)
            conexion.commit()
            id_trakbd = str(row[0])
            ordenes_query_insert ="INSERT INTO ordenes(frase_objetiva, tipo_orden, sin1, sin2, sin3, sin4, id_camp, url_diff, fechaini, fechafinal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id_trakbd,1,"sin","sin","sin","sin",id_campana,ulr_insert,"2020-01-07","2020-01-07")
            cursed = conexion.cursor(buffered=True)
            cursed.execute(ordenes_query_insert,val)
            conexion.commit()
            print("Insert de Ordenes")
            print("\n")
            

tbodyseoc = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr')
#boton de ideas
ctbodyseoc = len(tbodyseoc)
for i in range(1,ctbodyseoc+1):
    vari = str(i)
    try:
        buttonideas = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div/div/table/tbody[2]/tr['+vari+']/td[6]/div/button').click()
    except NoSuchElementException:
        print("Nada mas que agregar")
    time.sleep(5)
    
#Strategy Features
    strategy_ideas = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/ul/li')
    strategy_ideas_len = len(strategy_ideas)
    for i in range(1,strategy_ideas_len+1):
        var_i = (str(i))  
        stra_span = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/ul/li['+var_i+']')
        about_var = "About"
        bodytag = "<body>" 
        reemplazar_por = "body"
        page = "'s"
        change_page = ""
        h1_hello = "<h1>"
        h1_bye = "h1"
        del_det = "See detailed analysis"
        del_why = "Why should I do this?"
        del_dif = "Difficulty:"
        nada = ""
        nada1 = ""
        nada2 = ""
        dont = "doesn't"
        dontf = "does not"
        content_aux = stra_span.text.replace(bodytag, reemplazar_por) 
        content_aux1 = content_aux.replace(page, change_page)
        content_aux2 = content_aux1.replace(h1_hello, h1_bye)
        content_aux3 = content_aux2.replace(del_det, nada)
        content_aux4 = content_aux3.replace(del_why, nada1)
        content_aux5 = content_aux4.replace(del_dif, nada2)
        stra_span_text = content_aux5.replace(dont, dontf)
        truefalse = about_var in stra_span_text
        if truefalse == True:
            print("Ninguna tarea que agregar parece que todo esta bien por aqui")
        else:
            query_tareas =  "select * from tareasred where detalles_tarea ="+com1+stra_span_text+com1
            cursed = conexion.cursor(buffered=True)
            cursed.execute(query_tareas)
            tareas_row = cursed.fetchall()
            tareas_row_len = cursed.rowcount
            if tareas_row_len == 1:
                print("Todas la tareas ya han sido agregadas")
            else:
                url_diff_task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/h2/span').text
                query_order = "select * from ordenes where url_diff ="+com1+url_diff_task+com1
                cursed = conexion.cursor(buffered=True)
                cursed.execute(query_order)
                ordenes_row = cursed.fetchall()
                for row_o in ordenes_row:
                    print(str(row_o[8]))
                    query = "INSERT INTO tareasred(id_orden, id_usuario, titulo_tarea,detalles_tarea, estado) VALUES (%s,%s,%s,%s,%s)"
                    val = (str(row_o[0]),1,stra_span_text,stra_span_text,0)
                    cursor.execute(query,val)
                    conexion.commit()  
                    print("Tarea Creada para redactor con exito")
            print("Texto Span Strategy: " + stra_span.text)
        print("\n")
#serp features
    serp_f = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div/ul/li')
    serp_len = len(serp_f)
    for i in range(1,serp_len+1):
        var_ser_i = str(i)
        page = "'s"
        change_page = " s"
        var_i_s = str(i)#contandor
        serp_span = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div/ul/li['+var_ser_i+']')
        bodytag = "<body>" 
        reemplazar_por = "body"
        page = "'s"
        change_page = ""
        h1_hello = "<h1>"
        h1_bye = "h1"
        del_det = "See detailed analysis"
        del_why = "Why should I do this?"
        del_dif = "Difficulty:"
        nada = ""
        nada1 = ""
        nada2 = ""
        dont = "doesn't"
        dontf = "does not"
        content_aux = serp_span.text.replace(bodytag, reemplazar_por) 
        content_aux1 = content_aux.replace(page, change_page)
        content_aux2 = content_aux1.replace(h1_hello, h1_bye)
        content_aux3 = content_aux2.replace(del_det, nada)
        content_aux4 = content_aux3.replace(del_why, nada1)
        content_aux5 = content_aux4.replace(del_dif, nada2)
        serp_span_text = content_aux5.replace(dont, dontf)
        truefalse_serp = about_var in serp_span_text
        if truefalse_serp == True:
            print("Ninguna tarea que agregar parece que todo esta bien por aqui")
        else:
            query_tareas =  "select * from tareasred where detalles_tarea ="+com1+serp_span_text+com1
            cursed = conexion.cursor(buffered=True)
            cursed.execute(query_tareas)
            tareas_row = cursed.fetchall()
            tareas_row_len = cursed.rowcount
            if tareas_row_len == 1:
                print("Todas la tareas ya han sido agregadas")
            else:
                url_diff_task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/h2/span').text
                query_order = "select * from ordenes where url_diff ="+com1+url_diff_task+com1
                cursed = conexion.cursor(buffered=True)
                cursed.execute(query_order)
                ordenes_row = cursed.fetchall()
                for row_o in ordenes_row:
                    print(str(row_o[8]))
                    query = "INSERT INTO tareasred(id_orden, id_usuario, titulo_tarea,detalles_tarea, estado) VALUES (%s,%s,%s,%s,%s)"
                    val = (str(row_o[0]),1,serp_span_text,serp_span_text,0)
                    cursor.execute(query,val)
                    conexion.commit()  
                    print("Tarea Creada para redactor con exito")
  
            print("Tareas Len: " + str(tareas_row_len))
            print("Se Guarda: "+ serp_span_text)
        print("\n")
# Content Features 

    content_f = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div[2]/div/div/div/ul/li')
    content_len = len(content_f)
    for i in range(1,content_len+1):
        var_i_c = str(i)#contandor
        content_li = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[4]/div[2]/div/div/div/ul/li['+var_i_c+']')
        about_var = "About"
        truefalse = about_var in content_li.text
        bodytag = "<body>" 
        reemplazar_por = "body"
        page = "'s"
        change_page = ""
        h1_hello = "<h1>"
        h1_bye = "h1"
        del_det = "See detailed analysis"
        del_why = "Why should I do this?"
        del_dif = "Difficulty:"
        nada = ""
        nada1 = ""
        nada2 = ""
        dont = "doesn't"
        dontf = "does not"
        content_aux = content_li.text.replace(bodytag, reemplazar_por) 
        content_aux1 = content_aux.replace(page, change_page)
        content_aux2 = content_aux1.replace(h1_hello, h1_bye)
        content_aux3 = content_aux2.replace(del_det, nada)
        content_aux4 = content_aux3.replace(del_why, nada1)
        content_aux5 = content_aux4.replace(del_dif, nada2)
        content_li_text = content_aux5.replace(dont, dontf)
        if truefalse == True:
            print("Ninguna tarea que agregar parece que todo esta bien por aqui")
        else:
            query_tareas =  "select * from tareasred where detalles_tarea ="+com1+content_li_text+com1
            cursed = conexion.cursor(buffered=True)
            cursed.execute(query_tareas)
            tareas_row = cursed.fetchall()
            tareas_row_len = cursed.rowcount
            if tareas_row_len == 1:
                print("Todas la tareas ya han sido agregadas")
            else:
                url_diff_task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/h2/span').text
                query_order = "select * from ordenes where url_diff ="+com1+url_diff_task+com1
                cursed = conexion.cursor(buffered=True)
                cursed.execute(query_order)
                ordenes_row = cursed.fetchall()
                for row_o in ordenes_row:
                    print(str(row_o[8]))
                    
                    if content_li_text == "":
                        print("Esta vacio")
                    else:
                        query = "INSERT INTO tareasred(id_orden, id_usuario, titulo_tarea,detalles_tarea, estado) VALUES (%s,%s,%s,%s,%s)"
                        val = (str(row_o[0]),1,content_li_text,content_li_text,0)
                        cursor.execute(query,val)
                        conexion.commit()  
                        print("Tarea Creada para redactor con exito Content")
            print("Content Text: "+content_li_text)
        print("\n")
# Semantic Features
    semantic_f = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[5]/div[2]/div/div/div/ul/li')
    semantic_len = len(semantic_f)
    for i in range(1,semantic_len+1):
        var_i_seman = str(i)
        bodytag = "<body>" 
        reemplazar_por = "body"
        page = "'s"
        change_page = ""
        h1_hello = "<h1>"
        h1_bye = "h1"
        del_det = "See detailed analysis"
        del_why = "Why should I do this?"
        del_dif = "Difficulty:"
        nada = ""
        nada1 = ""
        nada2 = ""
        dont = "doesn't"
        dontf = "does not"
        semantic_li = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[5]/div[2]/div/div/div/ul/li['+var_i_seman+']')
        semantic_li_aux = semantic_li.text.replace(bodytag, reemplazar_por) 
        semantic_li_aux1 = semantic_li_aux.replace(page, change_page)
        semantic_li_aux2 = semantic_li_aux1.replace(h1_hello, h1_bye)
        semantic_li_aux3 = semantic_li_aux2.replace(del_det, nada)
        semantic_li_aux4 = semantic_li_aux3.replace(del_why, nada1)
        semantic_li_aux5 = semantic_li_aux4.replace(del_dif, nada2)
        semantic_li_text = semantic_li_aux5.replace(dont, dontf).rstrip('\n')
        truefalse_sem = about_var in semantic_li_text
        if truefalse_sem == True:
            print("Nada que agregar")
        else:
            query_tareas =  "select * from tareasred where detalles_tarea ="+com1+semantic_li_text+com1
            cursed = conexion.cursor(buffered=True)
            cursed.execute(query_tareas)
            tareas_row = cursed.fetchall()
            tareas_row_len = cursed.rowcount
            if tareas_row_len == 1:
                print("Todas la tareas ya han sido agregadas")  
            else:
                url_diff_task = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/h2/span').text
                query_order = "select * from ordenes where url_diff ="+com1+url_diff_task+com1
                cursed = conexion.cursor(buffered=True)
                cursed.execute(query_order)
                ordenes_row = cursed.fetchall()
                for row_o in ordenes_row:
                    print(str(row_o[8]))
                    if semantic_li_text == "":
                        print("Esta vacio")
                    else:
                        query = "INSERT INTO tareasred(id_orden, id_usuario, titulo_tarea,detalles_tarea, estado) VALUES (%s,%s,%s,%s,%s)"
                        val = (str(row_o[0]),1,semantic_li_text,semantic_li_text,0)
                        cursor.execute(query,val)
                        conexion.commit()  
                        print("Tarea Creada para redactor con exito Para Semantic")
                        print("Semantic Text: "+semantic_li_text)               
        print("\n")
# technical Features 
    technical_f = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[7]/div[2]/div/div/div/ul/li')
    technical_len = len(technical_f)
    for i in range(1,technical_len+1):
        var_i_t = str(i)
        technical_li = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/div[7]/div[2]/div/div/div/ul/li['+var_i_t+']')
        technical_li_text = technical_li.text
        print("technical Text: "+technical_li_text[6:])
        print("\n")
    time.sleep(5)
    try:
        backtof = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[3]/div/a/button').click()
    except NoSuchElementException:
        print("Fin de las tareas")
    
    time.sleep(5)
#re run campaing
button_re = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/span[1]/button').click()
#site audit module
driver.get("https://www.semrush.com/siteaudit/campaign/"+urlcambiar+"/review/#overview")
time.sleep(4)
puntuacion = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/div[1]/div[1]/div[1]/div/div[2]').text
quitar_p = "%"
end_p = ""
puntuacion_to_number = int(puntuacion.replace(quitar_p,end_p))
print("Site Health: "+puntuacion)

if puntuacion_to_number <= 89:
    print("Some work to do")
    driver.get("https://www.semrush.com/siteaudit/campaign/"+urlcambiar+"/review/#issues")
    all_table_errors = driver.find_elements_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[1]/ul/li')
    all_table_warnings = driver.find_elements_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[2]/ul/li')
    all_table_notice = driver.find_elements_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[3]/ul/li')
    all_table_errors_len = len(all_table_errors)
    all_table_warnings_len = len(all_table_warnings)
    all_table_notice_len = len(all_table_notice)
    #errors
    print("Errors Tasks")
    for i in range(1,all_table_errors_len+1):
        var_i_errors = str(i)
        quitar_a = u'’'
        end_a = ""
        element = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[1]/ul/li['+var_i_errors+']').text.replace(quitar_a,end_a)
        sendToTrello = "Send to Trello"
        trueFalse = sendToTrello in element
        if trueFalse == True:
            time.sleep(1)
            element_click = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[1]/ul/li['+var_i_errors+']/span[1]').click()
            time.sleep(2)
            quitar_1 = "Why and how to fix it"
            quitar_2 = "Send to Trello"
            replace_1 = ""
            
            titulo_task = driver.find_element_by_xpath('//*[@id="sa-wrapperHeaderDetailReport"]/div[2]/div[1]').text.replace(quitar_1,replace_1)
            titulo_task_s = titulo_task.replace(quitar_2,replace_1).rstrip('\n')
            all_table_internal = driver.find_elements_by_xpath('//*[@id="sa-wrapperTableDetailReport"]/div[2]/div[2]/div/table/tr')
            all_table_internal = len(all_table_internal)
            for i in range(1,all_table_internal+1):
                var_i_notice = str(i)
                time.sleep(2)
                page_url_text = driver.find_element_by_xpath('//*[@id="sa-wrapperTableDetailReport"]/div[2]/div[2]/div/table/tr['+var_i_notice+']').text
                quitar_b = u"•"
                replace_1 = ""
                page_url = page_url_text.replace(quitar_b,replace_1)
                if page_url == "":
                        print("Esta vacio")
                else:
                    print("Titulo de la tarea: "+ titulo_task_s + " Page url: " + page_url)
                    
            driver.get('https://www.semrush.com/siteaudit/campaign/'+urlcambiar+'/review/#issues')
        else:
            print("Warning buena Nro: "+var_i_errors+ ": " + element)
    print("\n")
    #warning
    print("Warning Tasks")
    for i in range(1,all_table_warnings_len+1):
        var_i_errors = str(i)
        quitar_a = u'’'
        end_a = ""
        element = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[2]/ul/li['+var_i_errors+']').text.replace(quitar_a,end_a)
        sendToTrello = "Send to Trello"
        trueFalse = sendToTrello in element
        if trueFalse == True:
            time.sleep(1)
            element_click = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[2]/ul/li['+var_i_errors+']/span[1]').click()
            time.sleep(2)
            quitar_1 = "Why and how to fix it"
            quitar_2 = "Send to Trello"
            replace_1 = ""
            
            titulo_task = driver.find_element_by_xpath('//*[@id="sa-wrapperHeaderDetailReport"]/div[2]/div[1]').text.replace(quitar_1,replace_1)
            titulo_task_s = titulo_task.replace(quitar_2,replace_1).rstrip('\n')
            all_table_internal = driver.find_elements_by_xpath('//*[@id="sa-wrapperTableDetailReport"]/div[2]/div[2]/div/table/tr')
            all_table_internal = len(all_table_internal)
            for i in range(1,all_table_internal+1):
                var_i_notice = str(i)
                time.sleep(2)
                page_url_text = driver.find_element_by_xpath('//*[@id="sa-wrapperTableDetailReport"]/div[2]/div[2]/div/table/tr['+var_i_notice+']').text
                quitar_b = u"•"
                replace_1 = ""
                page_url = page_url_text.replace(quitar_b,replace_1)
                if page_url == "":
                        print("Esta vacio")
                else:
                    print("Titulo de la tarea: "+ titulo_task_s + " Page url: " + page_url)
                    
            driver.get('https://www.semrush.com/siteaudit/campaign/'+urlcambiar+'/review/#issues')
        else:
            print("Warning buena Nro: "+var_i_errors+ ": " + element)
    print("\n")
    # #notice
    # print("Notice Tasks")
    # for i in range(1,all_table_notice_len+1):
    #     var_i_errors = str(i)
    #     quitar_a = u'’'
    #     quitar_b = u'•'
    #     end_a = ""
    #     element = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[3]/ul/li['+var_i_errors+']').text.replace(quitar_a,end_a)
    #     sendToTrello = "Send to Trello"
    #     trueFalse = sendToTrello in element
    #     if trueFalse == True:
    #         time.sleep(1)
    #         element_click = driver.find_element_by_xpath('//*[@id="issues-stacks"]/div/dl/dd[3]/ul/li['+str(i)+']/span[1]/a').click()
    #         time.sleep(2)
    #         quitar_1 = "Why and how to fix it"
    #         quitar_2 = "Send to Trello"
    #         replace_1 = ""
            
    #         titulo_task = driver.find_element_by_xpath('//*[@id="sa-wrapperHeaderDetailReport"]/div[2]/div[1]').text.replace(quitar_1,replace_1)
    #         titulo_task_s = titulo_task.replace(quitar_2,replace_1).rstrip('\n')
    #         all_table_internal = driver.find_elements_by_xpath('//*[@id="sa-wrapperTableDetailReport"]/div[2]/div[2]/div/table/tr')
    #         all_table_internal = len(all_table_internal)
    #         for i in range(1,all_table_internal+1):
    #             var_i_notice = str(i)
    #             time.sleep(2)
    #             page_url_text = driver.find_element_by_xpath('//*[@id="sa-wrapperTableDetailReport"]/div[2]/div[2]/div/table/tr['+var_i_notice+']').text
    #             quitar_b = u"•"
    #             replace_1 = ""
    #             page_url = page_url_text.replace(quitar_b,replace_1)
    #             if page_url == "":
    #                     print("Esta vacio")
    #             else:
    #                 print("Titulo de la tarea: "+ titulo_task_s + " Page url: " + page_url)
                    
    #         driver.get('https://www.semrush.com/siteaudit/campaign/'+urlcambiar+'/review/#issues')
    #     else:
    #         print("Notice buena Nro: "+var_i_errors+ ": " + element)
    # print("\n")
else:
    print("Great nothig to do :)")
print("Fin del Script")



