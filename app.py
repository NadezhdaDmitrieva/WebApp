from fastapi import FastAPI, Depends # пишу импорт
import psycopg2 
import uvicorn
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
import os #для чтения переменных окружения
from dotenv import load_dotenv
 
app = FastAPI() # создаю приложение

def get_db():
    print('*********zero***********')
    return psycopg2.connect(
        database=os.environ.get("POSTGRES_DATABASE"),         # меняю startml на os.environ.get[""POSTGRES_DATABASE""]
        user=os.environ.get("POSTGRES_USER"),              # меняю "robot-startml-ro" на =os.environ.get["POSTGRES.USER"] чтобы из консоли пользователь мог ввести данные и в открытом коде небыли явно данные о пароле и др данных базы данных,
        password=os.environ.get("POSTGRES_PASSWORD"),     #"pheiph0hahj1Vaif", на os.environ.get["POSTGRES.PASSWORD"] 
        host=os.environ.get("POSTGRES_HOST"),               #"postgres.lab.karpov.courses",
        port=os.environ.get("POSTGRES_PORT")           #6432 ЗАМЕНИЛА НА os.environ.get["POSTGRES.PORT"]
    )

'''Можно еще так:
    return psycopg2.connect(
        database=os.environ["POSTGRES_DATABASE"],         # меняю startml на os.environ.get[""POSTGRES_DATABASE""]
        user=os.environ["POSTGRES_USER"],              # меняю "robot-startml-ro" на =os.environ.get["POSTGRES.USER"] чтобы из консоли пользователь мог ввести данные и в открытом коде небыли явно данные о пароле и др данных базы данных,
        password=os.environ["POSTGRES_PASSWORD"],     #"pheiph0hahj1Vaif", на os.environ.get["POSTGRES.PASSWORD"] 
        host=os.environ["POSTGRES_HOST"],               #"postgres.lab.karpov.courses",
        port=os.environ["POSTGRES_PORT"]          #6432 ЗАМЕНИЛА НА os.environ.get["POSTGRES.PORT"]
    )
    '''

@app.get("/user") #создаем get запрос(pet point), который будет доставать всех users из базы данных
def get_all_users(limit: int = 10, db: connection = Depends(get_db)):
    print("*******one******")
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        print("*******two******")
        cursor.execute(f"""
            SELECT *
            FROM "user"
            LIMIT{limit}
            """)
        print("*******three******")
        return cursor.fetchall()

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app)