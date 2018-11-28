import rows, os, django, sqlite3
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eleicoes2018.settings")
django.setup()

from candidatos.models import Candidato, Candidatura, Cargo, Coligacao, Coligacao_Partidos, Eleicao, Estado_Nascimento, Local_Eleicao, Municipio, Partido, Turno_Eleicao

dir = os.path.abspath('.')
dir_arquivos_csv = os.path.join(dir, 'consulta_cand_2018/')
arquivos_csv = [ os.path.join(dir_arquivos_csv, nome_arquivo) for nome_arquivo in os.listdir(dir_arquivos_csv) if 'candidatos' in nome_arquivo ]

def popular_dados_partidos():
    i = 0
    csv_partidos = rows.import_from_csv('consulta_cand_2018/partidos_politicos.csv', encoding='latin-1')

    for partido in csv_partidos:
        i += 1
        sigla = partido.sigla
        nome_partido = partido.partido
        numero_partido = partido.numero

        p = Partido.objects.create(
            sigla_partido = sigla,
            nome_partido = nome_partido,
            numero_partido = numero_partido,
        )

        p.save()
        print('%s' %(sigla))


def popular_dados_eleicao():
    for arquivo in arquivos_csv:
        i = 0
        csv_eleicoes = rows.import_from_csv(arquivo, encoding='latin-1')

        print(arquivo)

        for linha in csv_eleicoes:
            i+=1
            # eleicao
            descricao_eleicao = linha.ds_eleicao
            ano = linha.ano_eleicao
            abrangencia = linha.tp_abrangencia

            try:
                eleicao = Eleicao.objects.get(desc_eleicao=descricao_eleicao)
            except Eleicao.DoesNotExist:
                eleicao = Eleicao.objects.create(
                    desc_eleicao=descricao_eleicao,
                    ano_eleicao = ano,
                    abrangencia = abrangencia,
                )
                eleicao.save()

            # local_eleicao
            uf_eleicao = linha.sg_ue
            nome_estado_eleicao = linha.nm_ue

            try:
                local_eleicao = Local_Eleicao.objects.get(abreviacao=uf_eleicao)
            except Local_Eleicao.DoesNotExist:
                local_eleicao = Local_Eleicao.objects.create(
                    abreviacao=uf_eleicao,
                    nome_local = nome_estado_eleicao,
                    eleicao = eleicao,
                )
                local_eleicao.save()

            # coligacao
            nome_coligacao = linha.nm_coligacao
            coligacao = linha.ds_composicao_coligacao.split(' / ')

            try:
                c = Coligacao.objects.get(nome_coligacao=nome_coligacao)
            except Coligacao.DoesNotExist:
                c = Coligacao.objects.create(
                    nome_coligacao=nome_coligacao,
                    local=local_eleicao
                )
                c.save()

            try:
                coligacao_partidos = Coligacao_Partidos.objects.create(coligacao = c)
                for partido in coligacao:
                    p = Partido.objects.get(sigla_partido=partido)
                    coligacao_partidos.partido.add(p)
                coligacao_partidos.save()
            except sqlite3.IntegrityError:
                pass

            #turno_eleicao
            turno_eleicao = linha.nr_turno
            data_eleicao = date(
                int(linha.dt_eleicao[6:]),
                int(linha.dt_eleicao[3:5]),
                int(linha.dt_eleicao[0:2]),
            )
            try:
                turno = Turno_Eleicao.objects.get(turno=turno_eleicao)
            except Turno_Eleicao.DoesNotExist:
                turno = Turno_Eleicao.objects.create(turno = turno_eleicao,
                                                     data_eleicao=data_eleicao)
                turno.save()

            # partido
            sigla = linha.sg_partido
            partido = Partido.objects.get(sigla_partido = sigla)

            #cargo
            desc_cargo = linha.ds_cargo
            try:
                cargo = Cargo.objects.get(desc_cargo=desc_cargo)
            except Cargo.DoesNotExist:
                cargo = Cargo.objects.create(desc_cargo=desc_cargo)
                cargo.save()

            #candidatura
            reeleicao = linha.st_reeleicao
            declaracao_bens = linha.st_declarar_bens
            resultado_candidato = linha.ds_sit_tot_turno

            candidatura = Candidatura.objects.create(
                reeleicao = reeleicao,
                declaracao_bens = declaracao_bens,
                resultado_eleicao = resultado_candidato,
            )
            candidatura.save()

            #local de nascimento
            municipio_nasc = linha.nm_municipio_nascimento
            uf_nasc = linha.sg_uf_nascimento

            try:
                estado_nasc = Estado_Nascimento.objects.get(UF=uf_nasc)
            except Estado_Nascimento.DoesNotExist:
                estado_nasc = Estado_Nascimento.objects.create(UF=uf_nasc)
                estado_nasc.save()

            try:
                municipio = Municipio.objects.get(nome_municipio=municipio_nasc)
            except Municipio.DoesNotExist:
                municipio = Municipio.objects.create(
                    nome_municipio=municipio_nasc,
                    UF=estado_nasc,
                )

            #candidato
            nome_candidato = linha.nm_candidato
            nome_urna_candidato = linha.nm_urna_candidato
            genero = linha.ds_genero
            grau_instrucao = linha.ds_grau_instrucao
            estado_civil = linha.ds_estado_civil
            idade_data_posse = linha.nr_idade_data_posse
            raca = linha.ds_cor_raca
            ocupacao = linha.ds_ocupacao
            email_contato = linha.nm_email
            nacionalidade = linha.ds_nacionalidade
            data_nasc = date(
                int(linha.dt_nascimento[6:]),
                int(linha.dt_nascimento[3:5]),
                int(linha.dt_nascimento[0:2]),
            )
            nr_urna_candidato = linha.nr_candidato

            try:
                candidato = Candidato.objects.create(
                    nome_completo = nome_candidato,
                    nome_urna = nome_urna_candidato,
                    genero = genero,
                    grau_instrucao = grau_instrucao,
                    estado_civil = estado_civil,
                    idade_data_posse = idade_data_posse,
                    raca = raca,
                    ocupacao = ocupacao,
                    email_contato = email_contato,
                    nacionalidade = nacionalidade,
                    data_nasc = data_nasc,
                    numero_candidato = nr_urna_candidato,
                    cargo = cargo,
                    partido = partido,
                    municipio = municipio,
                    candidatura = candidatura,
                    local_eleicao = local_eleicao,
                )
                candidato.save()
            except sqlite3.IntegrityError:
                pass

            print('%d - %s' % (i, nome_urna_candidato))


if __name__ == '__main__':
    os.system('rm -rf db.sqlite3')
    os.system('python manage.py makemigrations candidatos')
    os.system('python manage.py migrate')

    print("Populando base de dados dos partidos...")
    popular_dados_partidos()
    print("\nPopulando base de dados dos candidatos...")
    popular_dados_eleicao()
