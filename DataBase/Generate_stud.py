with open(r'Data_proj\implantout.json', encoding='utf-8') as file:
    track = 0
    for ligne in file:
        if track < 370000:
            effectif=random.randint(300,5000)
            try:
                etab = json.loads(ligne)
                for i in range(effectif):
                    track+=1
                    d=create_student(etab["fields"]["coordonnees"], data_etud, bourse_tracker0, sexe_tracker0, etab["fields"]["services"])
                    data_etud["features"].append(d)


            except KeyError:
                continue
    print(track)

with open('data_stud.geojson', 'w', encoding='utf-8') as outfile:
    json.dump(data_etud, outfile, ensure_ascii=False)