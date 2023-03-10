from datetime import datetime
from pathlib import Path
from typing import Optional

from db import database
from pythagoras import Pythagoras
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def index(
        request: Request,
        lang: Optional[str] = None,
        bday: Optional[str] = None
):
    if bday is None:
        if request.cookies:
            lang_id = request.cookies['formData'][-1]
        else:
            lang_id = 0
        print(lang_id)
        if lang_id is not None:
            lang_dict = {'0': 'en', '1': 'de', '2': 'ua', '3': 'ru'}
            diff = f"SELECT info_{lang_dict[str(lang_id)]} FROM different_info"
            diff = await database.fetch_all(query=diff)
            diff = [item[0] for item in diff]

        context = {
            "request": request,
            'lang': lang,
            'info': diff[23],
            'enter_name': diff[45].replace('&apos;', "'"),
            'enter_birthday': diff[46],
            'show_calc': diff[47],
            'calc_table': diff[6],
            'description':diff[48].replace('&apos;', "'"),
        }
        return templates.TemplateResponse("home.html", context)

    if lang:
        abt = f"SELECT info_{lang} FROM about_info"
        diff = f"SELECT info_{lang} FROM different_info"
        full = f"SELECT name, info_{lang} FROM full_info"
        gen = f"SELECT info_{lang} FROM general_info"
        lines = f"SELECT info_{lang} FROM lines_info"
    else:
        abt = "SELECT info_en FROM about_info"
        diff = "SELECT info_en FROM different_info"
        full = "SELECT name, info_en FROM full_info"
        gen = "SELECT info_en FROM general_info"
        lines = "SELECT info_en FROM lines_info"

    # READ TABLES FROM DB
    abt = await database.fetch_all(query=abt)
    abt = [item[0] for item in abt]

    diff = await database.fetch_all(query=diff)
    diff = [item[0] for item in diff]

    full = await database.fetch_all(query=full)
    full = {key[0]: key[1] for key in full}

    gen = await database.fetch_all(query=gen)
    gen = [item[0] for item in gen]
    gen = '<br><br>'.join(gen)

    lines = await database.fetch_all(query=lines)
    lines = [item[0] for item in lines]
    try:
        dte = datetime.strptime(bday, '%Y-%m-%d').date()
    except:
        return {'Message': 'Wrong date entered!'}
    pythagoras = Pythagoras(dte.day, dte.month, dte.year)

    p = pythagoras.nums

    butt1 = full['1'] if len(p[0]) == 0 else full[p[0]] if len(p[0]) < 6 else full['111111']
    butt2 = full['2-0'] if len(p[1]) == 0 else full[p[1]] if len(p[1]) < 4 else full['2222']
    butt3 = full['3-0'] if len(p[2]) == 0 else full[p[2]] if len(p[2]) < 4 else full['3333']
    butt4 = full['4-0'] if len(p[3]) == 0 else full[p[3]] if len(p[3]) < 2 else full['44']
    butt5 = full['5-0'] if len(p[4]) == 0 else full[p[4]] if len(p[4]) < 3 else full['555']
    butt6 = full['6-0'] if len(p[5]) == 0 else full[p[5]] if len(p[5]) < 3 else full['666']
    butt7 = full['7-0'] if len(p[6]) == 0 else full[p[6]] if len(p[6]) < 3 else full['777']
    butt8 = full['8-0'] if len(p[7]) == 0 else full[p[7]] if len(p[7]) < 2 else full['88']
    butt9 = full['9'] if len(p[8]) == 0 else full[p[8]] if len(p[8]) < 3 else full['999']

    context = {

        'about_compatibility': abt[0],
        'about_my': abt[1],
        'about_general': abt[2],

        'year_2000': diff[0],
        'first_num': diff[1],
        'second_num': diff[2],
        'third_num': diff[3],
        'forth_num': diff[4],
        'embodiment': diff[5],
        'calc_table': diff[6],
        'name': diff[7],
        'birthday': diff[8],
        'head_pythagoras': diff[9],
        'work_num': diff[10],
        'first_num_name': diff[11],
        'second_num_name': diff[12],
        'third_num_name': diff[13],
        'forth_num_name': diff[14],
        'colums_name': diff[15],
        'first_col_name': diff[16],
        'second_col_name': diff[17],
        'third_col_name': diff[18],
        'diag_name': diff[19],
        'diag_down_name': diff[20],
        'diag_up_name': diff[21],
        'embodiment_name': diff[22],
        'translated_info': diff[23],
        'title': diff[24],
        'strings_name': diff[25],
        'first_string': diff[26],
        'second_string': diff[27],
        'third_string': diff[28],
        'one_char': diff[29],
        'two_energy': diff[30],
        'three_science': diff[31],
        'four_health': diff[32].replace('&apos;', "'"),
        'five_logic': diff[33],
        'six_skills': diff[34],
        'seven_luck': diff[35],
        'eight_duty': diff[36],
        'nine_memory': diff[37].replace('&apos;', "'"),
        'about_dev': diff[38],
        'about_author': diff[39],
        'about_compat': diff[40],
        'gen_info_name': diff[41],
        'comp_calc': diff[42],
        'back_home': diff[43],
        'm_click': diff[44],
        'table_description': diff[49].replace('&apos;', "'"),

        'butt1': butt1,
        'butt2': butt2,
        'butt3': butt3,
        'butt4': butt4,
        'butt5': butt5,
        'butt6': butt6,
        'butt7': butt7,
        'butt8': butt8,
        'butt9': butt9,

        # 'gen1': gen[0],
        # 'gen2': gen[1],
        # 'gen3': gen[2],
        # 'gen4': gen[3],
        # 'gen5': gen[4],
        # 'gen6': gen[5],
        # 'gen7': gen[6],
        # 'gen8': gen[7],
        # 'gen9': gen[8],

        'gen': gen,

        'horizontal_1': lines[0],
        'horizontal_2': lines[1],
        'horizontal_3': lines[2],
        'vertical_1': lines[3],
        'vertical_2': lines[4],
        'vertical_3': lines[5],
        'diag_down': lines[6],
        'diag_up': lines[7],

        "request": request,
        'nums': pythagoras.nums,
        'var': pythagoras.variables,
        'lang': lang
    }
    return templates.TemplateResponse("index.html", context)

