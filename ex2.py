time = int(input("Сколько секунд до счастья? : "))
hours=time// 3600
minutes= (time//60)-(hours*60)
sec= time % 60
print(f"До счастья осталось: {hours:02}:{minutes:02}:{sec:02}")