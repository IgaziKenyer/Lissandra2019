# LissandraBot
import discord
from discord.ext import commands
import asyncio
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from googleapiclient.discovery import build
#from pprint import pprint

# arcane solution
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
#creds = ServiceAccountCredentials.from_json_keyfile_name("Gremio-ddcc51ef0d6d.json", scope)
creds = json.loads(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
with open('gcreds.json', 'w') as fp:
    json.dump(creds,fp)
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('gcreds.json', scope)
drive = GooogleDrive(gauth)
client = gspread.authorize(creds)





sheet = client.open("Gremiotest").sheet1
wks3 = client.open("Gremiotest").get_worksheet(2)
data3 = wks3.get_all_records()
data = sheet.get_all_records()  # Get a list of all records
wks2 = client.open("Gremiotest").get_worksheet(1)
data2 = wks2.get_all_records()

# row = sheet.row_values(3)  # Get a specific row
# col = sheet.col_values(3)  # Get a specific column
# cell = sheet.cell(1,2).value  # Get the value of a specific cell

# insertRow = ["hello", 5, "red", "blue"]
# sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

# sheet.update_cell(2,2, "CHANGED")  # Update one cell

# numRows = sheet.row_count  # Get the number of rows in the sheet

# gremiocharacterstats@gremio.iam.gserviceaccount.com
# Sheets AIzaSyAKMpdAEsBTrYJXKSdjVT3hvOzefSbyAy4
client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    print('Lissandra is Ready')


# @client.event
# async def on_command_error(error, ctx):
#    await ctx.send(" Lo siento, no estas autorizado para esa accion")


@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: ping pong!')
    print('Usuario uso ping!')


list_of_lists = sheet.get_all_values()


@client.command()
async def Mostrar(ctx, arg1):
    #	await ctx.send

    # cell_list = sheet.findall(arg)
    # Si Args es igual a Personaje then list of list es ese numero.

    #NombreAventurero =
    cell = sheet.find(arg1)
    row = cell.row
    values_list = sheet.row_values(row)
    #await ctx.send(values_list[1])
    embed = discord.Embed(title= "Estado de Aventurero")
    embed.add_field(
        name= "Nombre",
        value= values_list[1]
         )
    embed.add_field(
        name="Raza",
        value=values_list[10]
    )

    embed.add_field(
        name="Elemento",
        value=values_list[11]
    )
    if values_list[5] == "Si":
        embed.add_field(
            name="Nivel Espiritual",
            value=values_list[4]
        )
    elif values_list[5] == "No":
        embed.add_field(
            name="\u200b",
            value="\u200b"
        )
    embed.add_field(
        name= "Estado",
        value=values_list[13]
    )
    embed.add_field(
        name="Nivel",
        value=values_list[7]
    )
    if values_list[10] == "Hombre Dragon":
        embed.add_field(
            name="Nivel Draconico",
            value=[8]

        )
    embed.add_field(
        name="Rango",
        value=values_list[14]
    )
    embed.add_field(
        name="Experiencia",
        value=values_list[6]
    )
    await ctx.send(embed=embed)
    # if arg == "Khurth":
    #     elemento = list_of_lists[1]
    #
    #     embed = discord.Embed(title='Estado de Aventurero', description='')
    #     embed.add_field(
    #         name="Nombre del Aventurero",
    #         value=elemento[1]
    #     )


    #     #embed.set_thumbnail()
    #     #embed.set_footer()
    #     await  ctx.send(embed=embed)
    #     #id = 1
    #     #await ctx.send(list_of_lists['id'])
    #
    # elif arg == "Chris":
    #     id = 3
    #     await ctx.send(list_of_lists[id])

@client.command()
async def Elemento(ctx, arg1):
    cell3 = wks3.find(arg1)
    row3 = cell3.row
    values_list3 = wks3.row_values(row3)

    embed = discord.Embed(title="Estado Espiritual")
    embed.add_field(
         name="Nombre",
         value=values_list3[0],

     )
    embed.add_field(
         name="Alma",
         value=values_list3[9]
     )
    if int(values_list3[1]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Fuego",
             value=icono + values_list3[1]
         )
    elif 199 >= int(values_list3[1]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Fuego",
             value=icono + values_list3[1]
         )
    elif 100 <= int(values_list3[1]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Fuego",
             value=icono + values_list3[1]
         )
    if int(values_list3[2]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Agua",
             value=icono + values_list3[2]
         )
    elif 199 >= int(values_list3[2]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Agua",
             value=icono + values_list3[2]
         )
    elif int(values_list3[2]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Agua",
             value=icono + values_list3[2]
         )
    if int(values_list3[3]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Tierra",
             value=icono + values_list3[3]
         )
    elif 199 >= int(values_list3[3]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Tierra",
             value=icono + values_list3[3]
         )
    elif 100 <= int(values_list3[3]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Tierra",
             value=icono + values_list3[3]
         )
    if int(values_list3[4]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Viento",
             value=icono + values_list3[4]
         )
    elif 199 >= int(values_list3[4]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Viento",
             value=icono + values_list3[4]
         )
    elif 100 <= int(values_list3[4]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Viento",
             value=icono + values_list3[4]
         )
    if int(values_list3[5]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Rayo",
             value=icono + values_list3[5]
         )
    elif 199 >= int(values_list3[5]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Rayo",
             value=icono + values_list3[5]
         )
    elif 100 <= int(values_list3[5]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Rayo",
             value=icono + values_list3[5]
         )
    if int(values_list3[6]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Planta",
             value=icono + values_list3[6]
         )
    elif 199 >= int(values_list3[6]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Planta",
             value=icono + values_list3[6]
         )
    elif 100 <= int(values_list3[6]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Planta",
             value=icono + values_list3[6]
         )
    if int(values_list3[7]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Oscuridad",
             value=icono + values_list3[7]
         )
    elif 199 >= int(values_list3[7]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Oscuridad",
             value=icono + values_list3[7]
         )
    elif 100 <= int(values_list3[7]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Oscuridad",
             value=icono + values_list3[7]
         )
    if int(values_list3[8]) <= 99: ##Sin Elemento
         icono = " "
         embed.add_field(
             name="Luz",
             value= icono + values_list3[8]
         )
    elif 199 >= int(values_list3[8]) >= 100: ##Con Elemento
         icono = ":diamond_shape_with_a_dot_inside:"
         embed.add_field(
             name="Luz",
             value= icono + values_list3[8]
         )
    elif 100 <= int(values_list3[8]) >= 200: ##Con Espiritual
         icono = "<:Avydia:587428651189010475>"
         embed.add_field(
             name="Luz",
             value=icono + values_list3[8]
         )
        ##Crear un Sistema para hacer resistencias?
    Fuego = values_list3[1]
    Agua = values_list3[2]
    Tierra = values_list3[3]
    Viento = values_list3[4]
    Rayo = values_list3[5]
    Planta = values_list3[6]
    Oscuridad = values_list3[7]
    Luz = values_list3[8]
    Debilidad = " "
    ElementalList=[values_list3[1],values_list3[2],values_list3[3],values_list3[4],values_list3[5],values_list3[6],values_list3[7],values_list3[8]]

    count = []
    contador = 0
    for value in ElementalList:
        num = float(value)
        if num >= 100:
            contador += 1
            print("Hay un Elemento Arriba de 100!!! Resistencia Elemental CHECK EN CAMINO")
            print(contador)


        ##

    if contador >= 2:
        ######################################Fuego VS Agua #################################
        def maximum1(Fuego, Agua):
            if int(Fuego) > int(Agua):
                return Fuego;
            else:
                return Agua;
        def minimum1(Fuego, Agua):
            if Fuego < Agua:
                return Fuego;
            else:
                return Agua;
        if int(Fuego) > int(Agua):
            Debilidad = "Agua"
        else:
            Debilidad = "Fuego"
        if Fuego == 0 or Agua == 0:
            Resistencia = 0
        else:
            Division = int(minimum1(Fuego, Agua)) / int(maximum1(Fuego, Agua))
            Resistencia = float(Division) * 100
        if Resistencia < 40:
            if values_list3[10] != "Fuego" and values_list3[10] != "Agua":
                if Resistencia <= 40 and Resistencia >= 30:
                    embed.add_field(
                        name= "Debilidad Elemental",
                        value= "Debilidad -2 Contra " + " " + Debilidad
                    )
                if Resistencia <= 29 and Resistencia >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad
                    )
                if Resistencia <= 19 and Resistencia >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad
                    )
                if Resistencia <= 9 and Resistencia >= 2:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad
                    )
                if Resistencia <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad
                    )
                #40 ~~~30 -2
                #29 ~~~20 -4
                #19 ~~ 10 -6
                #9 ~~~ 2 x 2
                #1 ~~~ 0 x 4
###############################################Viento VS Tierra#############################
        def maximum2(Viento, Tierra):
            if int(Viento) > int(Tierra):
                return Viento;
            else:
                return Tierra;
        def minimum2(Viento, Tierra):
            if Viento < Tierra:
                return Viento;
            else:
                return Tierra;
        if int(Viento) > int(Tierra):
            Debilidad2 = "Tierra"
        else:
            Debilidad2 = "Viento"
        if Viento == 0 or Tierra == 0:
            Resistencia2 = 0
        else:
            Division2 = int(minimum2(Viento, Tierra)) / int(maximum2(Viento, Tierra))
            Resistencia2 = float(Division2) * 100
        if Resistencia2 < 40:
            if values_list3[10] != "Viento" and values_list3[10] != "Tierra":
                if Resistencia2 <= 40 and Resistencia2 >= 30:
                    embed.add_field(
                        name= "Debilidad Elemental",
                        value= "Debilidad -2 Contra " + " " + Debilidad2
                    )
                if Resistencia2 <= 29 and Resistencia2 >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad2
                    )
                if Resistencia2 <= 19 and Resistencia2 >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad2
                    )
                if Resistencia2 <= 9 and Resistencia2 >= 2:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad2
                    )
                if Resistencia2 <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad2
                    )
###############################################Rayo VS Planta#################################
        def maximum3(Rayo, Planta):
            if int(Rayo) > int(Planta):
                return Rayo;
            else:
                return Planta;
        def minimum3(Rayo, Planta):
            if Rayo < Planta:
                return Rayo;
            else:
                return Planta;
        if int(Rayo) > int(Planta):
            Debilidad3 = "Planta"
        else:
            Debilidad3 = "Rayo"
        if Rayo == 0 or Planta == 0:
            Resistencia3 = 0
        else:
            Division3 = int(minimum3(Rayo, Planta)) / int(maximum3(Rayo, Planta))
            Resistencia3 = float(Division3) * 100
        if Resistencia3 < 40:
            if values_list3[10] != "Rayo" and values_list3[10] != "Planta":
                if Resistencia3 <= 40 and Resistencia3 >= 30:
                    embed.add_field(
                        name= "Debilidad Elemental",
                        value= "Debilidad -2 Contra " + " " + Debilidad3
                    )
                if Resistencia3 <= 29 and Resistencia3 >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad3
                    )
                if Resistencia3 <= 19 and Resistencia3 >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad3
                    )
                if Resistencia3 <= 9 and Resistencia3 >= 2:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad3
                    )
                if Resistencia3 <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad3
                    )
###############################################Oscuridad VS Luz#############################
        def maximum4(Oscuridad, Luz):
            if int(Oscuridad) > int(Luz):
                return Oscuridad;
            else:
                return Luz;
        def minimum4(Oscuridad, Luz):
            if Oscuridad < Luz:
                return Oscuridad;
            else:
                return Luz;
        if int(Oscuridad) > int(Luz):
            Debilidad4 = "Oscuridad"
        else:
            Debilidad4 = "Luz"

        if Oscuridad == 0 or Luz == 0:
            Resistencia4 = 0
            print("Oscuridad or Luz 0 ")
        else:
            Division4 = int(minimum4(Oscuridad, Luz)) / int(maximum4(Oscuridad, Luz))
            Resistencia4 = float(Division4) * 100
        if Resistencia4 < 40:
            print( Resistencia4)
            if values_list3[10] != "Oscuridad" and values_list3[10] != "Luz":
                if Resistencia <= 40 and Resistencia4 >= 30:
                    embed.add_field(
                        name= "Debilidad Elemental",
                        value= "Debilidad -2 Contra " + " " + Debilidad4
                    )
                if Resistencia4 <= 29 and Resistencia4 >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad4
                    )
                if Resistencia4 <= 19 and Resistencia4 >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad4
                    )
                if Resistencia4 <= 9 and Resistencia4 >= 2:
                    print("Debilidad elemental x2")
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad4
                    )
                if  Resistencia4 <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad4
                    )

    await ctx.send(embed=embed)
@client.command()
@commands.has_role("Game Master")
async def TrueSight(ctx, arg1,):
    cell3 = wks3.find(arg1)
    row3 = cell3.row
    values_list3 = wks3.row_values(row3)

    embed = discord.Embed(title="Estado Espiritual")
    embed.add_field(
        name="Nombre",
        value=values_list3[0],

    )
    embed.add_field(
        name="Alma",
        value=values_list3[9]
    )
    if int(values_list3[1]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Fuego",
            value=icono + values_list3[1]
        )
    elif 199 >= int(values_list3[1]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Fuego",
            value=icono + values_list3[1]
        )
    elif 100 <= int(values_list3[1]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Fuego",
            value=icono + values_list3[1]
        )
    if int(values_list3[2]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Agua",
            value=icono + values_list3[2]
        )
    elif 199 >= int(values_list3[2]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Agua",
            value=icono + values_list3[2]
        )
    elif int(values_list3[2]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Agua",
            value=icono + values_list3[2]
        )
    if int(values_list3[3]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Tierra",
            value=icono + values_list3[3]
        )
    elif 199 >= int(values_list3[3]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Tierra",
            value=icono + values_list3[3]
        )
    elif 100 <= int(values_list3[3]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Tierra",
            value=icono + values_list3[3]
        )
    if int(values_list3[4]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Viento",
            value=icono + values_list3[4]
        )
    elif 199 >= int(values_list3[4]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Viento",
            value=icono + values_list3[4]
        )
    elif 100 <= int(values_list3[4]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Viento",
            value=icono + values_list3[4]
        )
    if int(values_list3[5]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Rayo",
            value=icono + values_list3[5]
        )
    elif 199 >= int(values_list3[5]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Rayo",
            value=icono + values_list3[5]
        )
    elif 100 <= int(values_list3[5]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Rayo",
            value=icono + values_list3[5]
        )
    if int(values_list3[6]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Planta",
            value=icono + values_list3[6]
        )
    elif 199 >= int(values_list3[6]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Planta",
            value=icono + values_list3[6]
        )
    elif 100 <= int(values_list3[6]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Planta",
            value=icono + values_list3[6]
        )
    if int(values_list3[7]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Oscuridad",
            value=icono + values_list3[7]
        )
    elif 199 >= int(values_list3[7]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Oscuridad",
            value=icono + values_list3[7]
        )
    elif 100 <= int(values_list3[7]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Oscuridad",
            value=icono + values_list3[7]
        )
    if int(values_list3[8]) <= 99:  ##Sin Elemento
        icono = " "
        embed.add_field(
            name="Luz",
            value=icono + values_list3[8]
        )
    elif 199 >= int(values_list3[8]) >= 100:  ##Con Elemento
        icono = ":diamond_shape_with_a_dot_inside:"
        embed.add_field(
            name="Luz",
            value=icono + values_list3[8]
        )
    elif 100 <= int(values_list3[8]) >= 200:  ##Con Espiritual
        icono = "<:Avydia:587428651189010475>"
        embed.add_field(
            name="Luz",
            value=icono + values_list3[8]
        )
    ##Crear un Sistema para hacer resistencias?
    Fuego = values_list3[1]
    Agua = values_list3[2]
    Tierra = values_list3[3]
    Viento = values_list3[4]
    Rayo = values_list3[5]
    Planta = values_list3[6]
    Oscuridad = values_list3[7]
    Luz = values_list3[8]
    Debilidad = " "
    ElementalList = [values_list3[1], values_list3[2], values_list3[3], values_list3[4], values_list3[5],
                     values_list3[6], values_list3[7], values_list3[8]]

    count = []
    contador = 0
    for value in ElementalList:
        num = float(value)
        if num >= 100:
            contador += 1
            print("Hay un Elemento Arriba de 100!!! Resistencia Elemental CHECK EN CAMINO")
            print(contador)

        ##

    if contador >= 2:
        ######################################Fuego VS Agua #################################
        def maximum1(Fuego, Agua):
            if int(Fuego) > int(Agua):
                return Fuego;
            else:
                return Agua;

        def minimum1(Fuego, Agua):
            if Fuego < Agua:
                return Fuego;
            else:
                return Agua;

        if int(Fuego) > int(Agua):
            Debilidad = "Agua"
        else:
            Debilidad = "Fuego"
        if Fuego == 0 or Agua == 0:
            Resistencia = 0
        else:
            Division = int(minimum1(Fuego, Agua)) / int(maximum1(Fuego, Agua))
            Resistencia = float(Division) * 100
        if Resistencia < 40:
            if values_list3[10] != "Fuego" and values_list3[10] != "Agua":
                if Resistencia <= 40 and Resistencia >= 30:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -2 Contra " + " " + Debilidad
                    )
                if Resistencia <= 29 and Resistencia >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad
                    )
                if Resistencia <= 19 and Resistencia >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad
                    )
                if Resistencia <= 9 and Resistencia >= 2:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad
                    )
                if Resistencia <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad
                    )
                # 40 ~~~30 -2
                # 29 ~~~20 -4
                # 19 ~~ 10 -6
                # 9 ~~~ 2 x 2
                # 1 ~~~ 0 x 4

        ###############################################Viento VS Tierra#############################
        def maximum2(Viento, Tierra):
            if int(Viento) > int(Tierra):
                return Viento;
            else:
                return Tierra;

        def minimum2(Viento, Tierra):
            if Viento < Tierra:
                return Viento;
            else:
                return Tierra;

        if int(Viento) > int(Tierra):
            Debilidad2 = "Tierra"
        else:
            Debilidad2 = "Viento"
        if Viento == 0 or Tierra == 0:
            Resistencia2 = 0
        else:
            Division2 = int(minimum2(Viento, Tierra)) / int(maximum2(Viento, Tierra))
            Resistencia2 = float(Division2) * 100
        if Resistencia2 < 40:
            if values_list3[10] != "Viento" and values_list3[10] != "Tierra":
                if Resistencia2 <= 40 and Resistencia2 >= 30:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -2 Contra " + " " + Debilidad2
                    )
                if Resistencia2 <= 29 and Resistencia2 >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad2
                    )
                if Resistencia2 <= 19 and Resistencia2 >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad2
                    )
                if Resistencia2 <= 9 and Resistencia2 >= 2:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad2
                    )
                if Resistencia2 <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad2
                    )

        ###############################################Rayo VS Planta#################################
        def maximum3(Rayo, Planta):
            if int(Rayo) > int(Planta):
                return Rayo;
            else:
                return Planta;

        def minimum3(Rayo, Planta):
            if Rayo < Planta:
                return Rayo;
            else:
                return Planta;

        if int(Rayo) > int(Planta):
            Debilidad3 = "Planta"
        else:
            Debilidad3 = "Rayo"
        if Rayo == 0 or Planta == 0:
            Resistencia3 = 0
        else:
            Division3 = int(minimum3(Rayo, Planta)) / int(maximum3(Rayo, Planta))
            Resistencia3 = float(Division3) * 100
        if Resistencia3 < 40:
            if values_list3[10] != "Rayo" and values_list3[10] != "Planta":
                if Resistencia3 <= 40 and Resistencia3 >= 30:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -2 Contra " + " " + Debilidad3
                    )
                if Resistencia3 <= 29 and Resistencia3 >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad3
                    )
                if Resistencia3 <= 19 and Resistencia3 >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad3
                    )
                if Resistencia3 <= 9 and Resistencia3 >= 2:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad3
                    )
                if Resistencia3 <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad3
                    )

        ###############################################Oscuridad VS Luz#############################
        def maximum4(Oscuridad, Luz):
            if int(Oscuridad) > int(Luz):
                return Oscuridad;
            else:
                return Luz;

        def minimum4(Oscuridad, Luz):
            if Oscuridad < Luz:
                return Oscuridad;
            else:
                return Luz;

        if int(Oscuridad) > int(Luz):
            Debilidad4 = "Oscuridad"
        else:
            Debilidad4 = "Luz"

        if Oscuridad == 0 or Luz == 0:
            Resistencia4 = 0
            print("Oscuridad or Luz 0 ")
        else:
            Division4 = int(minimum4(Oscuridad, Luz)) / int(maximum4(Oscuridad, Luz))
            Resistencia4 = float(Division4) * 100
        if Resistencia4 < 40:
            print(Resistencia4)
            if values_list3[10] != "Oscuridad" and values_list3[10] != "Luz":
                if Resistencia <= 40 and Resistencia4 >= 30:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -2 Contra " + " " + Debilidad4
                    )
                if Resistencia4 <= 29 and Resistencia4 >= 20:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -4 Contra" + " " + Debilidad4
                    )
                if Resistencia4 <= 19 and Resistencia4 >= 10:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad -6 Contra" + " " + Debilidad4
                    )
                if Resistencia4 <= 9 and Resistencia4 >= 2:
                    print("Debilidad elemental x2")
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad x2 Contra" + " " + Debilidad4
                    )
                if Resistencia4 <= 1:
                    embed.add_field(
                        name="Debilidad Elemental",
                        value="Debilidad Elemental x4 Contra" + " " + Debilidad4
                    )

        await ctx.send(embed=embed)

@client.command()
@commands.has_role("Game Master")
async def Modoro(ctx, arg1, arg2,):
    cell = sheet.find(arg1)
    row = cell.row
    col = int(cell.col) + 14
    values_list = sheet.row_values(row)
    OroActual = values_list[15]
    OroOperation = int(OroActual) + int(arg2)
    print(OroOperation)
    sheet.update_cell(row, col, OroOperation)
    print(OroActual)
    print(row)
    if int(OroActual) > int(OroOperation):
        await ctx.send("Perdiste" + " " + arg2 + "de Oro")
    else:
        await ctx.send("Ganaste" + " " + arg2 + "de Oro")

@client.command()
async def Mosoro(ctx, arg1):
    #Muestra el Oro de un Personaje
    cell = sheet.find(arg1)
    row = cell.row
    values_list = sheet.row_values(row)
    OroPersonaje = values_list[15]
    await ctx.send(arg1 + " " + "Tiene" + " " + OroPersonaje +" de Oro :lemon: "  )
#@client.commands()
#async def Gremero(ctx):
    #Muestra El Balance del Gremio Por Mes

@client.command()
async def Gremoro(ctx):
    ##Muestra La cantidad de Oro Actual del Gremio
    OroGremioLocation = "B38"
    OroDrogasLocation = "B39"
    OroMisionesLocation = "B40"
    TortugaDragonLocation = "B43"
    OroBancaLocation = "B44"

    OroGremio = wks2.acell(OroGremioLocation).value #Oro que el gremio gana por mes
    OroDrogas = wks2.acell(OroDrogasLocation).value # Oro que el gremio gana por medios ilegales
    OroMisiones = wks2.acell(OroMisionesLocation).value # Oro por misiones de los miembros
    OroTotal = int(OroGremio) + int(OroDrogas) + int(OroMisiones)
    TortugaDragon = wks2.acell(TortugaDragonLocation).value
    OroBanca = wks2.acell(OroBancaLocation).value
    embed = discord.Embed(title="Balance del Gremio El Loto Negro Nuevo Mes")

    embed.add_field(
        name="Ganacias por el Reino",
        value=OroGremio
    )
    embed.add_field(
        name="\u200b",
        value="\u200b"
    )
    embed.add_field(
        name="\u200b",
        value="\u200b"
    )

    embed.add_field(
        name="Ganancias Ilegales Mensuales",
        value= OroDrogas,
    )
    embed.add_field(
        name="\u200b",
        value="\u200b"
    )
    embed.add_field(
        name="\u200b",
        value="\u200b"
    )
    embed.add_field(
        name="Misiones de miembros",
        value= OroMisiones,
    )
    embed.add_field(
        name="\u200b",
        value="\u200b"
    )
    embed.add_field(
        name="\u200b",
        value="\u200b"
    )
    embed.add_field(
        name="Oro Total por Mes",
        value= OroTotal,
    )
    embed.add_field(
        name="Oro Total del Gremio",
        value= OroBanca
    )
    embed.add_field(
        name="Oro Actual de Tortuga Dragon",
        value= TortugaDragon,
    )
    await ctx.send(embed=embed)

@client.command()
@commands.has_role("Game Master")
async def Gremes(ctx):
    OroGremioLocation = "B38"
    OroDrogasLocation = "B39"
    OroMisionesLocation = "B40"
    TortugaDragonLocation = "B43"
    OroGremio = wks2.acell(OroGremioLocation).value  # Oro que el gremio gana por mes
    OroDrogas = wks2.acell(OroDrogasLocation).value  # Oro que el gremio gana por medios ilegales
    OroMisiones = wks2.acell(OroMisionesLocation).value  # Oro por misiones de los miembros
    OroTotal = int(OroGremio) + int(OroDrogas) + int(OroMisiones)
    TortugaDragon = wks2.acell(TortugaDragonLocation).value  # Oro Actual
    NewMonthGremio = int(OroGremio) + int(OroGremio)
    NewMonthDrogas = int(OroDrogas) + int(OroDrogas)
    NewMisiones = int(OroMisiones)+ int(OroMisiones)
    NewTotal = int(NewMonthGremio) + int(NewMonthDrogas) + int(NewMisiones)
    Banca = int(OroTotal) + int(NewTotal)
    wks2.update_acell('B38', NewMonthGremio)
    wks2.update_acell('B39', NewMonthDrogas)
    wks2.update_acell('B40', NewMisiones)
    wks2.update_acell('B44', Banca)

    embed = discord.Embed(title="Balance del Gremio El Loto Negro Nuevo Mes")

    embed.add_field(
        name="Ganacias por el Reino Pasado",
        value=OroGremio
    )
    embed.add_field(
        name="Ganancias por el Reino Este Mes",
        value=NewMonthGremio
    )

    embed.add_field(
        name="Ganancias Ilegales Mes Pasado",
        value=OroDrogas,
    )
    embed.add_field(
        name="Ganancias Ilegales de este Mes",
        value=NewMonthDrogas
    )

    embed.add_field(
        name="Misiones de miembros Mes Pasado",
        value=OroMisiones,
    )
    embed.add_field(
        name="Misiones de miembros este Mes",
        value=NewMisiones
    )

    embed.add_field(
        name="Oro Total Mes Pasado",
        value=OroTotal,
    )
    embed.add_field(
        name="Oro Total Este Mes",
        value=NewTotal
    )
    embed.add_field(
        name="Oro Total del Gremio",
        value=Banca
    )
    embed.add_field(
        name="Oro Actual de Tortuga Dragon",
        value=TortugaDragon,
    )
    await ctx.send(embed=embed)


#@client.commands()
#async def Adgromoro(ctx):
    #Agrega Oro al Gremio

#@client.commands()
#async def Mgremio(ctx, arg1):
    #Muestra a un miembro del gremio



@client.command()
async def Exp(ctx, arg1, arg2,):
    cell = sheet.find(arg1)
    row = cell.row
    col = cell.col
    values_list = sheet.row_values(row)
    colExp = cell.col + 5
    colLvL = cell.col + 6
    ExpActual = values_list[6]
    ExpGanada = int(values_list[6]) + int(arg2)
    LevelActual = values_list[7]
    print(ExpGanada)
    sheet.update_cell(row, colExp, ExpGanada)
    if int(values_list[6]) < 40:
        print("Menor que 40")
        NivelNuevo = int(ExpGanada) / int(5) + 1
        if int(LevelActual) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel ")
        if int(LevelActual) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelActual)
            NuevoValorNivel = int(LevelActual) + int(Diferencia)
            sheet.update_cell(row, colLvL, int(NuevoValorNivel))
            val3 = sheet.cell(row, colLvL,).value
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
    elif 68 > int(ExpGanada) >= 40:
        EXP7 = int(ExpGanada) - 40
        EXP7DIV = int(EXP7) / 7
        NivelNuevo = int(EXP7DIV) + 9
        print("LevelActual ")
        print(LevelActual)
        print("Nivel Nuevo")
        print(NivelNuevo)
        if int(LevelActual) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelActual) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelActual)
            NuevoValorNivel = int(LevelActual) + int(Diferencia)
            sheet.update_cell(row, colLvL, int(NuevoValorNivel))
            val3 = sheet.cell(row, colLvL).value
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
    elif 103 > int(ExpGanada) >= 68:
        EXP7 = int(ExpGanada)
        EXP7DIV = int(EXP7) / 8
        NivelNuevo = int(EXP7DIV) + 13
        if int(LevelActual) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelActual) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelActual)
            NuevoValorNivel = int(LevelActual) + int(Diferencia)
            sheet.update_cell(row, colLvL, int(NuevoValorNivel))
            val3 = sheet.cell(row, colLvL).value
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
    elif int(ExpGanada) >= 103:
        EXP7 = int(ExpGanada) - 103
        EXP7DIV = int(ExpGanada) / 17
        NivelNuevo = int(EXP7DIV) + 17
        if int(LevelActual) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelActual) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelActual)
            NuevoValorNivel = int(LevelActual) + int(Diferencia)
            sheet.update_cell(row, colLvL, int(NuevoValorNivel))
            val3 = sheet.cell(row, colLvL).value
            await  ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)

@client.command()
async def Poderes(ctx):
    url = 'http://powerlisting.wikia.com/wiki/Special:Random'
    embed = discord.Embed(title="Poder al Azar", description="Powerlisting wikia")
    embed.add_field(name="Poder", value=url)
    await ctx.send(embed=embed)

@client.command()
@commands.has_role("Game Master")
async def Exp2(ctx, arg1, arg2,):
    cell = sheet.find(arg1)
    row = cell.row
    col = cell.col
    values_list = sheet.row_values(row)
    ExpLocation = values_list[6]  # Cambiar dependiendo del Personaje
    LvlLocation = values_list[7]  # Cambiar dependiendo del Personaje
    #val = sheet.acell(ExpLocation).value  # El Valor de la EXP en G12
    sheet.update_acell(values_list[5])
    LevelCerrado = values_list[7]
    sheet.update_acell(values_list[6], int(ExpLocation) + int(arg2))  # El Valor de la EXP (val) + La Exp Agregada(arg)
    val2 = sheet.acell(ExpLocation).value  # La Nueva Exp
     ##Poner un IF en caso de que la EXP sea cierta cantidad para Legendario
     ##
    LevelAsker = int(LevelCerrado) + 1
    if int(sheet.acell(ExpLocation).value) < 40:
        print(sheet.acell((ExpLocation)).value)
        NivelNuevo = int(val2) / int(5) + 1
        if int(LevelCerrado) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelCerrado) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelCerrado)
            NuevoValorNivel = int(LevelCerrado) + int(Diferencia)
            sheet.update_acell(LvlLocation, int(NuevoValorNivel))
            val3 = sheet.acell(LvlLocation).value
            #          LevelCerrado = sheet.acell(LvlLocation, int(val3) + int(Diferencia))
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
        # await ctx.send(LevelAsker)


         #       await ctx.send (arg1 + "Subio" + Diferencia + "Niveles")
    elif 68 > int(val2) >= 40:
        EXP7 = int(val2) - 40
        EXP7DIV = int(EXP7) / 7
        NivelNuevo = int(EXP7DIV) + 9
        print("Estas en el Loop 7")
        if int(LevelCerrado) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelCerrado) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelCerrado)
            # NuevoValorNivel = int(LevelCerrado) + int(Diferencia)
            sheet.update_acell(LvlLocation, int(NivelNuevo))
            val3 = sheet.acell(LvlLocation).value
            #   LevelCerrado = sheet.acell(LvlLocation, int(val3) + int(Diferencia))
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
        #   await ctx.send (arg1 + "Subio" + Diferencia )
        ##HACER LO MISMO PARA LOS SIGUIENTES NIVELES
    elif 103 > int(val2) >= 68:
        EXP7 = int(val2) - 68
        EXP7DIV = int(EXP7) / 8
        NivelNuevo = int(EXP7DIV) + 13
        print("Estas en el Loop 8")
        if int(LevelCerrado) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelCerrado) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelCerrado)
            # NuevoValorNivel = int(LevelCerrado) + int(Diferencia)
            sheet.update_acell(LvlLocation, int(NivelNuevo))
            val3 = sheet.acell(LvlLocation).value
            #   LevelCerrado = sheet.acell(LvlLocation, int(val3) + int(Diferencia))
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
        #   await ctx.send (arg1 + "Subio" + Diferencia )
       ##HACER LO MISMO PARA LOS SIGUIENTES NIVELES
    elif int(val2) >= 103:
        EXP7 = int(val2) - 103
        EXP7DIV = int(EXP7) / 17
        NivelNuevo = int(EXP7DIV) + 17
        print("Estas en el Loop 9")
        if int(LevelCerrado) == int(NivelNuevo):
            await ctx.send(arg1 + " " + "No subio de Nivel")
        if int(LevelCerrado) < int(NivelNuevo):
            Diferencia = int(NivelNuevo) - int(LevelCerrado)
            # NuevoValorNivel = int(LevelCerrado) + int(Diferencia)
            sheet.update_acell(LvlLocation, int(NivelNuevo))
            val3 = sheet.acell(LvlLocation).value
            #   LevelCerrado = sheet.acell(LvlLocation, int(val3) + int(Diferencia))
            await ctx.send(arg1 + " " + "Subio al Nivel" + " " + val3)
            #   await ctx.send (arg1 + "Subio" + Diferencia )
            ##HACER LO MISMO PARA LOS SIGUIENTES NIVELES


# LevelValue = sheet.acell(LvlLocation).value
# if LevelCerrado < LevelValue:
#   val3 = sheet.acell(LvlLocation).value
#  await ctx.send(arg1 + "Subio al Nivel" + val3)
# if int(val2) >= 5: #EXP / 5

#   sheet.update_acell(LvlLocation,int(LevelValue) + 1 )
#   val3 = sheet.acell(LvlLocation).value
#   await ctx.send( arg1 + "Subio al Nivel" + val3)


# 2 Arguments NAME AND EXP [>Exp Landazuri 3]
#@Exp.error
#async def info_error(ctx, error):
#    await ctx.send('Lo siento no puedo permitirte acceder a esos documentos.')
#    if isinstance(error, commands.BadArgument):
#        await ctx.send('Lo Siento no puedo permitirte acceder a esos documentos.')


# @client.command()
# async def ping(ctx):
#	await ctx.send('Pong!')
@client.command()
async def Csitenno(
        ctx):  # api_adress = "http://api.openweathermap.org/data/2.5/appid=a677e1f4b9195e2b3437318ea0473e74&q="
    api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=1814906&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'  # city = input("City Name:")
    data = requests.get(api_adress)  # url = api_adress + city
    read = data.json()  # json_data = requests.get(url).json()
    icon = read['list'][0]['weather'][0]['icon']  # formated_data = json_data['weather'][0]['main']
    if icon in ['01d', '02n']:  # print(json_data)
        icono = ':sunny:'
        await ctx.send(':sunny:')
    elif icon in ['02d', '02n']:
        await ctx.send(':partly_sunny:')  # Cambiar la id para otra ciudad
        icono = ':partly_sunny:'  # Sitenno = Ciudad de Guayana, Venezuela
    elif icon in ['03d', '03n']:  # Kamikune = Hangzhou, China
        await ctx.send(':white_sun_cloud:')  # Shinko = Chongqing, China
        icono = ':white_sun_cloud:'  # Reino del Sur = Santiago, Chile
    elif icon in ['04d', '04n']:  # Gigaran =
        await ctx.send(':cloud:')  # Rhyn = Facativa, Colombia
        icono = ':cloud:'  # Krouzen = Bern
    elif icon in ['09d', '09n']:  # Roudesh = Munich, Germany
        await ctx.send(':white_sun_rain_cloud:')  # Jungla de las Pestes = Manaus, Brazil
        icono = ':white_sun_rain_cloud:'
    elif icon in ['10d', '10n']:
        await ctx.send(':cloud_rain: ')
        icono = ':cloud_rain: '
    elif icon in ['11d', '11n']:
        await ctx.send(':thunder_cloud_rain:')  # await bot.say ("Sitenno ")
        icono = ':thunder_cloud_rain:'  # await bot.say ("El clima actual es de {}".format(read['list'][0]['weather'][0]["description"]))
    elif icon in ['13d', '13n']:
        await ctx.send(':cloud_snow:')  # 01d/01n Soleado
        icono = ':cloud_snow:'  # 02d/02n algunas nubes :partly_sunny:
    elif icon in ['50d', '50n']:  # 03d/03n nubes esparcidas :white_sun_cloud:
        await ctx.send(':fog:')  # 04d/04n nubes rotas :cloud:
        icono = ':fog'  # 09d/09n Llovisna :white_sun_rain_cloud:
    embed = discord.Embed(title='Clima de Sitenno', description='')  # 010d/10n Lluvioso :cloud_rain:
    embed.add_field(
        name='En la ciudad de Sitenno el Clima actual es',
        value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
        inline=True)  # 011d/11n Tormenta de Rayos :thunder_cloud_rain:
    embed.add_field(
        name='La Temperatura actual es de',
        value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
        inline=True)  # 13d/13n Nieve :cloud_snow:
    embed.add_field(
        name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']),
        inline=True)  # 50d/50n Neblina :fog:
    embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
    embed.add_field(
        name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
    embed.set_thumbnail(url='https://i.imgur.com/heRUwq4.jpg')
    embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
    await ctx.send(embed=embed)



@client.command()
async def Ckamikune(ctx):
    api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=1808926&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'
    data = requests.get(api_adress)
    read = data.json()
    icon = read['list'][0]['weather'][0]['icon']
    if icon in ['01d', '01n']:
        icono = ':sunny:'
        await ctx.send(':sunny:')
    elif icon in ['02d', '02n']:
        await ctx.send(':partly_sunny:')
        icono = ':partly_sunny:'
    elif icon in ['03d', '03n']:
        await ctx.send(':white_sun_cloud:')
        icono = ':white_sun_cloud:'
    elif icon in ['04d', '04n']:
        await ctx.send(':cloud:')
        icono = ':cloud:'
    elif icon in ['09d', '09n']:
        await ctx.send(':white_sun_rain_cloud:')
        icono = ':white_sun_rain_cloud:'
    elif icon in ['10d',
                  '10n']:  # await bot.say ("La temperatura actual es de {}°C".format(read['list'][0]['main']["temp"]))
        await ctx.send(
            ':cloud_rain: '
        )  # await bot.say ("La minima y maxima para hoy seran {}°C".format(read['list'][0]["main"]["temp_min"]))
        icono = ':cloud_rain: '  # await bot.say ("h{}°C".format(read['list'][0]["main"]["temp_max"]))
    elif icon in ['11d', '11n']:  # Tempamin = read['list'][0]['main']["temp_min"]
        await ctx.send(':thunder_cloud_rain:')  # Tempamax = read['list'][0]['main']["temp_max"]
        icono = ':thunder_cloud_rain:'  # Temp_maxmin = Tempamin, "/", Tempamax
    elif icon in ['13d', '13n']:  # Humedad
        await ctx.send(
            ':cloud_snow:')  # await bot.say ("Con una humedad de {}%".format(read['list'][0]["main"]["humidity"]))
        icono = ':cloud_snow:'  # embed = discord.Embed(title="Clima", description= "En la ciudad de Sitenno el Clima actual es")
    elif icon in ['50d', '50n']:  # embed.add_field(name="icon", value=(read['list'][0]['weather'][0]["description"])
        await ctx.send(':fog:')  # await bot.say(embed=embed)
        icono = ':fog'
    embed = discord.Embed(title='Clima de Kamikune', description='')
    embed.add_field(
        name='En la ciudad de Kamikune el Clima actual es',
        value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
        inline=True)
    embed.add_field(
        name='La Temperatura actual es de',
        value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
        inline=True)
    embed.add_field(
        name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
    embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
    embed.add_field(
        name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
    embed.set_thumbnail(url='https://i.imgur.com/uHPfcbo.jpg')
    embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
    await ctx.send(embed=embed)
    print(icon)
    print(icono)


@client.command()
async def Cshinko(ctx):
    api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=1814906&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'
    data = requests.get(api_adress)
    read = data.json()
    icon = read['list'][0]['weather'][0]['icon']
    if icon in ['01d', '01n']:
        icono = ':sunny:'
        await ctx.send(':sunny:')
    elif icon in ['02d', '02n']:
        await ctx.send(':partly_sunny:')
        icono = ':partly_sunny:'
    elif icon in ['03d', '03n']:
        await ctx.send(':white_sun_cloud:')
        icono = ':white_sun_cloud:'
    elif icon in ['04d', '04n']:
        await ctx.send(':cloud:')
        icono = ':cloud:'
    elif icon in ['09d', '09n']:
        await ctx.send(':white_sun_rain_cloud:')
        icono = ':white_sun_rain_cloud:'
    elif icon in ['10d', '10n']:
        await ctx.send(':cloud_rain: ')
        icono = ':cloud_rain: '
    elif icon in ['11d', '11n']:
        await ctx.send(':thunder_cloud_rain:')
        icono = ':thunder_cloud_rain:'
    elif icon in ['13d', '13n']:
        await ctx.send(':cloud_snow:')
        icono = ':cloud_snow:'
    elif icon in ['50d', '50n']:
        await ctx.send(':fog:')
        icono = ':fog'
    embed = discord.Embed(title='Clima de Shinko', description='')
    embed.add_field(
        name='En la ciudad de Shinko el Clima actual es',
        value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
        inline=True)
    embed.add_field(
        name='La Temperatura actual es de',
        value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
        inline=True)
    embed.add_field(
        name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
    embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
    embed.add_field(
        name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
    embed.set_thumbnail(url='https://i.imgur.com/Qg12qfs.jpg')
    embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
    await ctx.send(embed=embed)
    print(icon)
    print(icono)


@client.command()
async def welp2(ctx):
    embed = discord.Embed(title="Ayuda")
    embed.add_field(
        name=">Mostrar [Nombre]",
        value= "Muestra los Datos del Personaje",
    )
    embed.add_field(
        name="Elemento [Nombre]",
        value="Muestra Datos Espirituales del Personaje",
    )
    embed.add_field(
        name=">Modoro [Nombre] [Cantidad]",
        value="Modifica la Cantidad de Oro del Personaje :name_badge:"
    )
    embed.add_field(
        name=">Mosoro [Nombre]",
        value="Muestra la Cantidad de Oro del Personaje"
    )
    embed.add_field(
        name=">Exp [Nombre] [Cantidad]",
        value="Otorga una cantidad de Exp al Personaje :name_badge:"
    )
    embed.add_field(
        name=">Gremoro",
        value="Muestra la Cantidad de Oro del Gremio"
    )
    embed.add_field(
        name="Gremes",
        value="Otorga Oro al Gremio por el cambio de Mes :name_badge:"

    )
    await ctx.send(embed=embed)

@client.command()
async def c(ctx, arg):
    if arg == 'sitenno':
        api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=1814906&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'
        data = requests.get(api_adress)
        read = data.json()
        icon = read['list'][0]['weather'][0]['icon']
        if icon in ['01d', '02n']:
            icono = ':sunny:'
            await ctx.send(':sunny:')
        elif icon in ['02d', '02n']:
            await ctx.send(':partly_sunny:')
            icono = ':partly_sunny:'
        elif icon in ['03d', '03n']:
            await ctx.send(':white_sun_cloud:')
            icono = ':white_sun_cloud:'
        elif icon in ['04d', '04n']:
            await ctx.send(':cloud:')
            icono = ':cloud:'
        elif icon in ['09d', '09n']:
            await ctx.send(':white_sun_rain_cloud:')
            icono = ':white_sun_rain_cloud:'
        elif icon in ['10d', '10n']:
            await ctx.send(':cloud_rain: ')
            icono = ':cloud_rain: '
        elif icon in ['11d', '11n']:
            await ctx.send(':thunder_cloud_rain:')
            icono = ':thunder_cloud_rain:'
        elif icon in ['13d', '13n']:
            await ctx.send(':cloud_snow:')
            icono = ':cloud_snow:'
        elif icon in ['50d', '50n']:
            await ctx.send(':fog:')
            icono = ':fog'
        embed = discord.Embed(title='Clima de Sitenno', description='')
        embed.add_field(
            name='En la ciudad de Sitenno el Clima actual es',
            value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
            inline=True)
        embed.add_field(
            name='La Temperatura actual es de',
            value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
            inline=True)
        embed.add_field(
            name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
        embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
        embed.add_field(
            name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
        embed.set_thumbnail(url='https://i.imgur.com/heRUwq4.jpg')
        embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
        await ctx.send(embed=embed)
    elif arg == 'kamikune':
        api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=1808926&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'
        data = requests.get(api_adress)
        read = data.json()
        icon = read['list'][0]['weather'][0]['icon']
        if icon in ['01d', '02n']:
            icono = ':sunny:'
            await ctx.send(':sunny:')
        elif icon in ['02d', '02n']:
            await ctx.send(':partly_sunny:')
            icono = ':partly_sunny:'
        elif icon in ['03d', '03n']:
            await ctx.send(':white_sun_cloud:')
            icono = ':white_sun_cloud:'
        elif icon in ['04d', '04n']:
            await ctx.send(':cloud:')
            icono = ':cloud:'
        elif icon in ['09d', '09n']:
            await ctx.send(':white_sun_rain_cloud:')
            icono = ':white_sun_rain_cloud:'
        elif icon in ['10d', '10n']:
            await ctx.send(':cloud_rain: ')
            icono = ':cloud_rain: '
        elif icon in ['11d', '11n']:
            await ctx.send(':thunder_cloud_rain:')
            icono = ':thunder_cloud_rain:'
        elif icon in ['13d', '13n']:
            await ctx.send(':cloud_snow:')
            icono = ':cloud_snow:'
        elif icon in ['50d', '50n']:
            await ctx.send(':fog:')
            icono = ':fog'
        embed = discord.Embed(title='Clima de Kamikune', description='')
        embed.add_field(
            name='En la ciudad de Kamikune el Clima actual es',
            value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
            inline=True)
        embed.add_field(
            name='La Temperatura actual es de',
            value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
            inline=True)
        embed.add_field(
            name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
        embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
        embed.add_field(
            name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
        embed.set_thumbnail(url='https://i.imgur.com/uHPfcbo.jpg')
        embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
        await ctx.send(embed=embed)
    elif arg == 'shinko':
        api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=1814906&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'
        data = requests.get(api_adress)
        read = data.json()
        icon = read['list'][0]['weather'][0]['icon']
        if icon in ['01d', '02n']:
            icono = ':sunny:'
            await ctx.send(':sunny:')
        elif icon in ['02d', '02n']:
            await ctx.send(':partly_sunny:')
            icono = ':partly_sunny:'
        elif icon in ['03d', '03n']:
            await ctx.send(':white_sun_cloud:')
            icono = ':white_sun_cloud:'
        elif icon in ['04d', '04n']:
            await ctx.send(':cloud:')
            icono = ':cloud:'
        elif icon in ['09d', '09n']:
            await ctx.send(':white_sun_rain_cloud:')
            icono = ':white_sun_rain_cloud:'
        elif icon in ['10d', '10n']:
            await ctx.send(':cloud_rain: ')
            icono = ':cloud_rain: '
        elif icon in ['11d', '11n']:
            await ctx.send(':thunder_cloud_rain:')
            icono = ':thunder_cloud_rain:'
        elif icon in ['13d', '13n']:
            await ctx.send(':cloud_snow:')
            icono = ':cloud_snow:'
        elif icon in ['50d', '50n']:
            await ctx.send(':fog:')
            icono = ':fog'
        embed = discord.Embed(title='Clima de Shinko', description='')
        embed.add_field(
            name='En la ciudad de Shinko el Clima actual es',
            value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
            inline=True)
        embed.add_field(
            name='La Temperatura actual es de',
            value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
            inline=True)
        embed.add_field(
            name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
        embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
        embed.add_field(
            name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
        embed.set_thumbnail(url='https://i.imgur.com/Qg12qfs.jpg')
        embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
        await ctx.send(embed=embed)
    elif arg == 'krouzen':
        api_adress = 'http://api.openweathermap.org/data/2.5/forecast?id=2661552&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'
        data = requests.get(api_adress)
        read = data.json()
        icon = read['list'][0]['weather'][0]['icon']
        if icon in ['01d', '01n']:
            icono = ':sunny:'
            await ctx.send(':sunny:')
        elif icon in ['02d', '02n']:
            await ctx.send(':partly_sunny:')
            icono = ':partly_sunny:'
        elif icon in ['03d', '03n']:
            await ctx.send(':white_sun_cloud:')
            icono = ':white_sun_cloud:'
        elif icon in ['04d', '04n']:
            await ctx.send(':cloud:')
            icono = ':cloud:'
        elif icon in ['09d', '09n']:
            await ctx.send(':white_sun_rain_cloud:')
            icono = ':white_sun_rain_cloud:'
        elif icon in ['10d', '10n']:
            await ctx.send(':cloud_rain: ')
            icono = ':cloud_rain: '
        elif icon in ['11d', '11n']:
            await ctx.send(':thunder_cloud_rain:')
            icono = ':thunder_cloud_rain:'
        elif icon in ['13d', '13n']:
            await ctx.send(':cloud_snow:')
            icono = ':cloud_snow:'
        elif icon in ['50d', '50n']:
            await ctx.send(':fog:')
            icono = ':fog'
        embed = discord.Embed(title='Clima de Krouzen', description='')
        embed.add_field(
            name='En la ciudad de Krouzen el Clima actual es',
            value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
            inline=True)
        embed.add_field(
            name='La Temperatura actual es de',
            value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
            inline=True)
        embed.add_field(
            name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
        embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
        embed.add_field(
            name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
        embed.set_thumbnail(url='https://i.imgur.com/4Qgz6G5.jpg')
        embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
        await ctx.send(embed=embed)
        print(icon)
        print(icono)
    else:
        api_adress = 'http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=a677e1f4b9195e2b3437318ea0473e74&lang=es&units=metric'.format(
            arg)
        data = requests.get(api_adress)
        read = data.json()
        icon = read['list'][0]['weather'][0]['icon']
        if icon in ['01d', '01n']:
            icono = ':sunny:'
            await ctx.send(':sunny:')
        elif icon in ['02d', '02n']:
            await ctx.send(':partly_sunny:')
            icono = ':partly_sunny:'
        elif icon in ['03d', '03n']:
            await ctx.send(':white_sun_cloud:')
            icono = ':white_sun_cloud:'
        elif icon in ['04d', '04n']:
            await ctx.send(':cloud:')
            icono = ':cloud:'
        elif icon in ['09d', '09n']:
            await ctx.send(':white_sun_rain_cloud:')
            icono = ':white_sun_rain_cloud:'
        elif icon in ['10d', '10n']:
            await ctx.send(':cloud_rain: ')
            icono = ':cloud_rain: '
        elif icon in ['11d', '11n']:
            await ctx.send(':thunder_cloud_rain:')
            icono = ':thunder_cloud_rain:'
        elif icon in ['13d', '13n']:
            await ctx.send(':cloud_snow:')
            icono = ':cloud_snow:'
        elif icon in ['50d', '50n']:
            await ctx.send(':fog:')
            icono = ':fog'
        embed = discord.Embed(title='Clima de {}'.format(arg), description='')
        embed.add_field(
            name='En la ciudad de {} el Clima actual es'.format(arg),
            value=icono + '{}'.format(read['list'][0]['weather'][0]['description']),
            inline=True)
        embed.add_field(
            name='La Temperatura actual es de',
            value='{}°C :thermometer:'.format(read['list'][0]['main']['temp']),
            inline=True)
        embed.add_field(
            name='La humedad es de', value='{}%:droplet:'.format(read['list'][0]['main']['humidity']), inline=True)
        embed.add_field(name='La maxima sera de', value='{}°C:arrow_up:'.format(read['list'][0]['main']['temp_max']))
        embed.add_field(
            name='La minima sera de', value='{}°C:arrow_down_small:'.format(read['list'][0]['main']['temp_min']))
        embed.set_footer(text='Informacion recopilada por el gremio de aventureros')
        await ctx.send(embed=embed)
        await ctx.send(arg)
        await ctx.send(arg)

    # @client.command(pass_context=True)
    # async def info(ctx, user: discord.Member):
    # embed = discord.Embed(title="{} info".format(user.name),
    #                      description="Esta es la informacion que tenemos en nuestros archivos.", color=0x00f00)
    # embed.add_field(name="Nombre", value=user.name, inline=True)
    # embed.add_field(name="ID", value=user.id, inline=True)
    # embed.add_field(name="Estado", value=user.status, inline=True)
    # embed.add_field(name="Rol mas alto", value=user.top_role, inline=True)
    # embed.add_field(name="Se unio el dia", value=user.joined_at, inline=True)
    # imageURL = "https://imgur.com/a/XJMZLP9"
    # embed.set_image(url=imageURL)
    # await client.say(embed=embed)
    # @client.command(pass_context=True)
    # async def embed(ctx):
    # embed = discord.Embed(title="test", description="Recepcionista del Gremio", color=0x00ff00)
    # embed.set_footer(text="this is the footer")
    # embed.set_author(name="Igazi Kenyer")
    # embed.add_field(name="This is a field", value="no, it isnt", inline=True)
    # await client.say(embed=embed)

    # @client.command()
    # async def welp(ctx):


#   embed = discord.Embed(title="Ayuda", description="Esta es la informacion que tenemos en nuestros archivos.",
#                         color=0x00f00)
# embed.add_field(name=">c [Ciudad]",
##                value='Comando para conocer el clima de ciertos lugares, lugares con nombres compuestos usar "[Ciu dad]" (sin los corchetes.). Actualmente debido a su localizacion puede obtener informacion de todas las ciudades de sus cercanias de Rha',
#                inline=True)
# embed.add_field(name="Lander",
#                value="Los lugares de Lander en los que tenemos este servicio son : Kamikune, Krouzen, Shinko, Sitenno y Rhyn ")
# embed.add_field(name=">info",
#                value="Para obtener informacion de un usuario, el usuario debe ser mencionado con @[NombredelUsuario]")
# embed.add_field(name=">poderes", value="Para obtener un poder al azar.")
# await client.say(embed=embed)
## @client.command(pass_context=True)
## async def poderes(ctx):
# url = URL.from_text(u'http://powerlisting.wikia.com/wiki/Special:Random')
#    embed = discord.Embed(title="Poder al Azar", description="Powerlisting wikia")
# embed.add_field(name="Poder", value=url)
# await client.say(embed=embed)




client.run('DISCORDKEY')
