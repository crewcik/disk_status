import psutil

print('Crew Disk Sistemi')
def disk_usage():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Disk İsim: {partition.device}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            if partition_usage.percent > 80:
                crew_mesaj = "Çok iyi"
            elif partition_usage.percent < 80:
                crew_mesaj = "İyi"
            elif partition_usage.percent < 50:
                crew_mesaj = "Kötü"
            elif partition_usage.percent < 20:
                crew_mesaj = "Çok kötü"
            print(f"Disk Boyutu: {partition_usage.total / (1024 ** 3):.2f} GB")
            print(f"Kullanılan Alan: {partition_usage.used / (1024 ** 3):.2f} GB")
            print(f"Boş Alan: {partition_usage.free / (1024 ** 3):.2f} GB")
            print(f"Disk Durumu: {partition_usage.percent}% : {crew_mesaj}\n")
        except PermissionError as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    disk_usage()
