from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def write_log(message: str):
    time.sleep(5)
    with open("log.txt",  mode="a") as log:
        log.write(f"Bildiris: {message}\n")
    print(f"Arxa plan isi tamamlandi: {message}")


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log,  f"Email gonderildi: {email}")

    return {"message": "Sorğunuz qəbul edildi. Arxa planda emal olunur."}
