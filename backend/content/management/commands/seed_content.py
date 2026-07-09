from django.core.management.base import BaseCommand

from content.models import (
    EducationEntry,
    ExperienceEntry,
    Institution,
    Profile,
    Project,
    Publication,
)


class Command(BaseCommand):
    help = "Seeds the database with Bruno Mingoti's real portfolio content (PT/EN)."

    def handle(self, *args, **options):
        self.seed_profile()
        self.seed_institutions()
        self.seed_projects()
        self.seed_publications()
        self.seed_experience()
        self.seed_education()
        self.stdout.write(self.style.SUCCESS("Seed completo."))

    def seed_profile(self):
        Profile.objects.update_or_create(
            pk=1,
            defaults=dict(
                name="Bruno Mingoti",
                headline_pt="Engenheiro Eletricista em formação — RWTH Aachen × UFSC",
                headline_en="Electrical Engineer in training — RWTH Aachen × UFSC",
                bio_pt=(
                    "Estou concluindo Engenharia Elétrica na UFSC (IAA 8,91/10,0) e me aproximo da entrada "
                    "no mercado de trabalho depois de uma trajetória construída entre laboratórios de pesquisa, "
                    "chão de fábrica e um intercâmbio de mais de um ano na Alemanha. Na Werkzeugmaschinenlabor "
                    "WZL da RWTH Aachen, escrevi meu TCC sobre reconstrução de tomografia industrial combinando "
                    "backprojection filtrada com denoising por deep learning, e desenvolvi dois pipelines "
                    "acelerados por GPU comparados ao software de referência do instituto — além de sistemas "
                    "backend/frontend para gestão automatizada de fluxos de dados de sensores e geração/validação "
                    "de Certificados Digitais de Calibração.\n\n"
                    "Antes disso, três anos como estagiário cooperado na Fundação CERTI, através do programa "
                    "NEO Empresarial, em parceria com empresas como WEG, Embraco/Nidec e Landis+Gyr. Ali minha "
                    "mentalidade de resolução de problemas foi moldada por projetos muito diferentes entre si: "
                    "firmware STM32 para disjuntores, visão computacional para detectar defeitos em notebooks, "
                    "uma aplicação supervisória que ajudou a economizar cerca de R$ 250 mil/ano na caldeiraria da "
                    "WEG, e modelos de detecção de objetos em imagens aéreas marítimas para apoiar buscas e "
                    "salvamentos — este último um projeto de cooperação Brasil-Suécia que também virou publicação "
                    "científica.\n\n"
                    "Viver e trabalhar na Alemanha, colaborando com equipes de pesquisa internacionais e "
                    "traduzindo problemas industriais complexos em soluções de dados, mudou a forma como penso "
                    "engenharia: menos sobre aplicar uma técnica específica e mais sobre entender o problema "
                    "certo antes de programar a solução. Hoje transito com naturalidade entre Python, TypeScript, "
                    "visão computacional, machine learning e sistemas embarcados — sempre com o mesmo instinto: "
                    "quebrar um problema difícil em partes que dá para testar, medir e melhorar."
                ),
                bio_en=(
                    "I'm finishing my Electrical Engineering degree at UFSC (GPA 8.91/10.0) and getting close to "
                    "entering the job market after a path built across research labs, factory floors, and a "
                    "year-plus exchange in Germany. At the Werkzeugmaschinenlabor WZL, RWTH Aachen, I wrote my "
                    "thesis on industrial CT reconstruction combining filtered backprojection with deep "
                    "learning-based sinogram denoising, implemented two GPU-accelerated pipelines benchmarked "
                    "against the institute's reference software, and built backend/frontend systems for "
                    "automated sensor data-stream management and for generating/validating Digital Calibration "
                    "Certificates.\n\n"
                    "Before that, three years as a co-op student at CERTI Foundation, through the NEO Empresarial "
                    "program, partnering with companies such as WEG, Embraco/Nidec, and Landis+Gyr. That's where "
                    "my problem-solving mindset was shaped by genuinely varied projects: STM32 firmware for "
                    "circuit breakers, computer vision to detect laptop defects, a supervisory application that "
                    "helped save an estimated €40k/year in WEG's boiler area, and object detection models over "
                    "aerial maritime imagery to support search-and-rescue missions — the latter a Brazil-Sweden "
                    "cooperation that also became a peer-reviewed publication.\n\n"
                    "Living and working in Germany, collaborating with international research teams and "
                    "translating complex industrial problems into data-driven solutions, changed how I think "
                    "about engineering: less about applying one specific technique, more about understanding the "
                    "right problem before writing the solution. Today I move comfortably between Python, "
                    "TypeScript, computer vision, machine learning, and embedded systems — always with the same "
                    "instinct: break a hard problem into pieces you can test, measure, and improve."
                ),
                email="brunomingoti@gmail.com",
                phone="+55 48 988336767",
                linkedin_url="https://www.linkedin.com/in/brunomingoti/",
                github_url="",
                scholar_url="https://scholar.google.com.br/citations?user=Dx-d55AAAAAJ&hl=pt-BR",
            ),
        )

    def seed_institutions(self):
        data = [
            ("wzl", "WZL — RWTH Aachen", 1),
            ("certi", "Fundação CERTI", 2),
            ("ufsc", "UFSC", 3),
            ("invest-jr", "Invest Jr.", 4),
        ]
        for slug, name, order in data:
            Institution.objects.update_or_create(slug=slug, defaults={"name": name, "order": order})

    def seed_projects(self):
        wzl = Institution.objects.get(slug="wzl")
        certi = Institution.objects.get(slug="certi")
        ufsc = Institution.objects.get(slug="ufsc")
        invest = Institution.objects.get(slug="invest-jr")

        projects = [
            dict(
                slug="ct-sinogram-denoising",
                title_pt="Reconstrução de CT industrial com denoising por deep learning",
                title_en="Industrial CT reconstruction with deep learning denoising",
                summary_pt="TCC: backprojection filtrada + denoising de sinogramas por deep learning, com pipelines aceleradas por GPU.",
                summary_en="Bachelor's thesis: filtered backprojection + deep learning sinogram denoising, with GPU-accelerated pipelines.",
                body_pt=(
                    "Trabalho de Conclusão de Curso desenvolvido na Werkzeugmaschinenlabor WZL da RWTH Aachen, "
                    "propondo combinar a reconstrução clássica por backprojection filtrada com um estágio de "
                    "denoising de sinogramas baseado em deep learning, visando melhorar a qualidade de "
                    "reconstrução de tomografia computadorizada industrial sem custo proibitivo de tempo.\n\n"
                    "Implementei duas pipelines de reconstrução aceleradas por GPU e as comparei, em benchmark "
                    "sistemático de qualidade e desempenho, contra o software de referência utilizado no "
                    "instituto — obtendo ganhos tanto em fidelidade da imagem reconstruída quanto em tempo de "
                    "processamento."
                ),
                body_en=(
                    "Bachelor's thesis developed at the Werkzeugmaschinenlabor WZL, RWTH Aachen, proposing to "
                    "combine classical filtered backprojection reconstruction with a deep learning-based sinogram "
                    "denoising stage, aiming to improve industrial CT reconstruction quality without a "
                    "prohibitive time cost.\n\n"
                    "I implemented two GPU-accelerated reconstruction pipelines and benchmarked them "
                    "systematically for quality and performance against the institute's reference software — "
                    "achieving gains in both reconstructed image fidelity and processing time."
                ),
                institution=wzl,
                role_pt="Assistente de Pesquisa (Hilfswissenschaftler)",
                role_en="Student Assistant (Hilfswissenschaftler)",
                period_start="2024-08",
                period_end="2025-12",
                tools="Python, PyTorch, GPU computing, CT reconstruction, deep learning",
                icon="ti-scan",
                featured=True,
                order=1,
            ),
            dict(
                slug="automated-data-stream-stack",
                title_pt="Automated Data Stream Management Software-Stack",
                title_en="Automated Data Stream Management Software-Stack",
                summary_pt="Serviços backend/frontend para matching automatizado de dispositivos, produtores e consumidores de dados.",
                summary_en="Backend/frontend services for automated device/producer/consumer data matching.",
                body_pt=(
                    "Software-stack desenvolvido no âmbito do projeto de pesquisa AMalytik (financiado pelo "
                    "Ministério Federal alemão de Assuntos Econômicos e Ação Climática), atuando como camada "
                    "intermediária dentro de um ecossistema SOIL, conectando dispositivos sensores (fontes de "
                    "dados) a aplicações consumidoras.\n\n"
                    "Desenvolvi tanto os serviços de backend quanto o frontend para o gerenciamento automatizado "
                    "desses fluxos de dados, incluindo o matching entre dispositivos, produtores e consumidores. "
                    "Código em Python e TypeScript, publicado com licença MIT e arquivado no Zenodo."
                ),
                body_en=(
                    "Software stack built as part of the AMalytik research project (funded by the German Federal "
                    "Ministry for Economic Affairs and Climate Action), acting as an intermediary layer within a "
                    "SOIL ecosystem, connecting sensor devices (data sources) to consumer applications.\n\n"
                    "I built both the backend services and the frontend for automated management of these data "
                    "flows, including device/producer/consumer matching. Code in Python and TypeScript, released "
                    "under the MIT license and archived on Zenodo."
                ),
                institution=wzl,
                role_pt="Assistente de Pesquisa (Hilfswissenschaftler)",
                role_en="Student Assistant (Hilfswissenschaftler)",
                period_start="2024-08",
                period_end="2025-12",
                tools="Python, TypeScript, REST APIs",
                icon="ti-topology-star-3",
                repo_url="https://zenodo.org/records/18255616",
                featured=True,
                order=2,
            ),
            dict(
                slug="dcc-generator-validator",
                title_pt="DCC Generator and Validator Webpage",
                title_en="DCC Generator and Validator Webpage",
                summary_pt="Geração e validação de Certificados Digitais de Calibração (DCC) em XML, com API REST e webapp.",
                summary_en="Generation and validation of Digital Calibration Certificates (DCC) XML, with a REST API and web app.",
                body_pt=(
                    "Ferramenta que converte dados de calibração em arquivos XML de Certificado Digital de "
                    "Calibração (DCC) compatíveis com o schema da PTB (Physikalisch-Technische Bundesanstalt), "
                    "com gestão de conteúdo tanto via API REST quanto interface web.\n\n"
                    "Implementei as operações de banco de dados para armazenamento e assinatura digital dos "
                    "conjuntos de medição, também no contexto do projeto AMalytik. Código em TypeScript e Python, "
                    "licença MIT, arquivado no Zenodo."
                ),
                body_en=(
                    "A tool that converts calibration data into standards-compliant Digital Calibration "
                    "Certificate (DCC) XML files following the PTB (Physikalisch-Technische Bundesanstalt) "
                    "schema, with content management through both a REST API and a web interface.\n\n"
                    "I implemented the database operations for storing and digitally signing measurement "
                    "datasets, also as part of the AMalytik project. Code in TypeScript and Python, MIT license, "
                    "archived on Zenodo."
                ),
                institution=wzl,
                role_pt="Assistente de Pesquisa (Hilfswissenschaftler)",
                role_en="Student Assistant (Hilfswissenschaftler)",
                period_start="2024-08",
                period_end="2025-12",
                tools="TypeScript, Python, digital signatures, REST APIs",
                icon="ti-certificate",
                repo_url="https://zenodo.org/records/18241584",
                order=3,
            ),
            dict(
                slug="maritime-search-rescue-detection",
                title_pt="Detecção de objetos em imagens aéreas marítimas para busca e salvamento",
                title_en="Object detection in aerial maritime images for search and rescue",
                summary_pt="Modelos de detecção e rastreamento para identificar destroços, embarcações e pessoas desaparecidas.",
                summary_en="Detection and tracking models to identify wrecks, vessels, and missing people at sea.",
                body_pt=(
                    "Projeto de cooperação Brasil-Suécia na área aeronáutica, com a Fundação CERTI, para usar IA "
                    "em missões de busca e salvamento. Desenvolvi modelos de detecção e rastreamento de objetos "
                    "em imagens aéreas marítimas, focados em identificar destroços, embarcações e pessoas "
                    "desaparecidas.\n\n"
                    "O trabalho deu origem à publicação 'Small Object Detection in Drone-Captured Images for "
                    "Maritime Surveillance', aceita no SIBGRAPI 2025."
                ),
                body_en=(
                    "A Brazil-Sweden cooperation project in Aeronautics, with CERTI Foundation, using AI to "
                    "support search-and-rescue missions. I developed object detection and tracking models over "
                    "aerial maritime imagery, focused on identifying wrecks, vessels, and missing people.\n\n"
                    "The work led to the publication 'Small Object Detection in Drone-Captured Images for "
                    "Maritime Surveillance', accepted at SIBGRAPI 2025."
                ),
                institution=certi,
                role_pt="Estagiário cooperado — Programa NEO Empresarial",
                role_en="Co-op student — NEO Empresarial program",
                period_start="2022-03",
                period_end="2024-07",
                tools="Python, computer vision, object detection, object tracking",
                icon="ti-drone",
                featured=True,
                order=4,
            ),
            dict(
                slug="weg-boiler-supervisory-app",
                title_pt="Aplicação supervisória para alívio de tensões térmicas (WEG)",
                title_en="Supervisory application for thermal stress relief (WEG)",
                summary_pt="App Electron + Modbus para a caldeiraria da WEG, com economia estimada de R$ 250 mil/ano.",
                summary_en="Electron + Modbus app for WEG's boiler area, with an estimated €40k/year in savings.",
                body_pt=(
                    "Desenvolvimento de uma aplicação supervisória em Electron, comunicando via protocolo Modbus, "
                    "para apoiar o processo de alívio de tensões térmicas na área de caldeiraria da WEG S.A. A "
                    "solução foi levada à produção, com economia estimada de R$ 250 mil por ano."
                ),
                body_en=(
                    "Built an Electron supervisory application communicating over Modbus to support the thermal "
                    "stress-relief process in WEG's boiler area. The solution went into production, with an "
                    "estimated €40k/year in savings."
                ),
                institution=certi,
                role_pt="Estagiário cooperado — Programa NEO Empresarial",
                role_en="Co-op student — NEO Empresarial program",
                period_start="2022-03",
                period_end="2024-07",
                tools="Electron, Modbus, industrial automation",
                icon="ti-flame",
                featured=True,
                order=5,
            ),
            dict(
                slug="stm32-breaker-firmware",
                title_pt="Firmware STM32 para disjuntores de caixa moldada (WEG)",
                title_en="STM32 firmware for molded-case circuit breakers (WEG)",
                summary_pt="Firmware em C para cálculos de disjuntores e comunicação I2C/SPI.",
                summary_en="C firmware for breaker tripping-curve calculations and I2C/SPI communication.",
                body_pt=(
                    "Desenvolvimento de firmware embarcado em C (STM32CubeIDE) para cálculos de disjuntores de "
                    "caixa moldada — incluindo curva de disparo — e comunicação via protocolos I2C/SPI, em "
                    "parceria com a WEG S.A."
                ),
                body_en=(
                    "Embedded firmware development in C (STM32CubeIDE) for molded-case circuit breaker "
                    "calculations — including the tripping curve — and I2C/SPI communication, in partnership "
                    "with WEG S.A."
                ),
                institution=certi,
                role_pt="Estagiário cooperado — Programa NEO Empresarial",
                role_en="Co-op student — NEO Empresarial program",
                period_start="2022-03",
                period_end="2024-07",
                tools="C, STM32CubeIDE, I2C, SPI, embedded systems",
                icon="ti-cpu",
                order=6,
            ),
            dict(
                slug="lenovo-defect-detection",
                title_pt="Detecção de defeitos em notebooks com YOLO (Lenovo)",
                title_en="Laptop defect detection with YOLO (Lenovo)",
                summary_pt="Sistema de visão computacional para identificar defeitos físicos em notebooks.",
                summary_en="Computer vision system to identify physical laptop defects.",
                body_pt=(
                    "Sistema de detecção de falhas usando YOLO para identificar defeitos físicos (manchas, "
                    "amassados) em notebooks, desenvolvido para a Lenovo em projeto na Fundação CERTI."
                ),
                body_en=(
                    "Failure-detection system using YOLO to identify physical defects (stains, dents) in "
                    "laptops, developed for Lenovo through a CERTI Foundation project."
                ),
                institution=certi,
                role_pt="Estagiário cooperado — Programa NEO Empresarial",
                role_en="Co-op student — NEO Empresarial program",
                period_start="2022-03",
                period_end="2024-07",
                tools="Python, YOLO, computer vision",
                icon="ti-device-laptop",
                order=7,
            ),
            dict(
                slug="vibration-spectrum-automation",
                title_pt="Automação de relatórios de espectro de vibração (WEG)",
                title_en="Vibration-spectrum reporting automation (WEG)",
                summary_pt="Automação implantada em produção para o WEG Motion Fleet Management.",
                summary_en="Automation deployed to production for WEG Motion Fleet Management.",
                body_pt=(
                    "Automação da análise e geração de relatórios de espectro de vibração para o WEG Motion "
                    "Fleet Management, padronizando dados de sensores em insights para tomada de decisão de "
                    "engenharia. Solução implantada em produção durante estágio de verão na WEG."
                ),
                body_en=(
                    "Automated vibration-spectrum analysis and reporting for WEG Motion Fleet Management, "
                    "transforming sensor data into standardized insights for engineering decision-making. "
                    "Deployed into production during a summer internship at WEG."
                ),
                institution=certi,
                role_pt="Estagiário cooperado — Programa NEO Empresarial",
                role_en="Co-op student — NEO Empresarial program",
                period_start="2022-03",
                period_end="2024-07",
                tools="Python, data pipelines, reporting",
                icon="ti-chart-dots",
                order=8,
            ),
            dict(
                slug="leukemia-cell-classification",
                title_pt="Classificação de células de leucemia linfoblástica aguda",
                title_en="Acute lymphoblastic leukemia cell classification",
                summary_pt="Ensemble InceptionV3 com weighted F1-score de 93,88%.",
                summary_en="InceptionV3 ensemble with 93.88% weighted F1-score.",
                body_pt=(
                    "Projeto acadêmico da UFSC de classificação de células de leucemia linfoblástica aguda a "
                    "partir de imagens, usando um ensemble de modelos InceptionV3. O modelo final atingiu "
                    "weighted F1-score de 93,88% no conjunto de teste."
                ),
                body_en=(
                    "UFSC academic project classifying acute lymphoblastic leukemia cells from images, using an "
                    "InceptionV3 model ensemble. The final model reached a 93.88% weighted F1-score on the test "
                    "set."
                ),
                institution=ufsc,
                role_pt="Projeto acadêmico",
                role_en="Academic project",
                period_start="2023",
                period_end="2024",
                tools="Python, TensorFlow, InceptionV3, ensemble learning",
                icon="ti-microscope",
                featured=True,
                order=9,
            ),
            dict(
                slug="he-tissue-segmentation",
                title_pt="Segmentação e estimativa de células em tecidos H&E",
                title_en="H&E tissue cell segmentation and estimation",
                summary_pt="Segmentação de imagens histológicas com OpenCV e scikit-image.",
                summary_en="Histology image segmentation with OpenCV and scikit-image.",
                body_pt=(
                    "Projeto acadêmico de processamento de imagens da UFSC voltado à segmentação e estimativa de "
                    "contagem de células em tecidos corados com Hematoxilina e Eosina (H&E), usando OpenCV e "
                    "scikit-image."
                ),
                body_en=(
                    "UFSC academic image-processing project focused on segmenting and estimating cell counts in "
                    "Hematoxylin and Eosin (H&E) stained tissue, using OpenCV and scikit-image."
                ),
                institution=ufsc,
                role_pt="Projeto acadêmico",
                role_en="Academic project",
                period_start="2023",
                period_end="2024",
                tools="Python, OpenCV, scikit-image",
                icon="ti-microscope",
                order=10,
            ),
            dict(
                slug="lithium-battery-model",
                title_pt="Levantamento de modelo simplificado de baterias de lítio",
                title_en="Simplified lithium-ion battery model identification",
                summary_pt="Identificação de parâmetros de bateria de lítio em laboratório, publicado no CBMAG 2024.",
                summary_en="Lab-based lithium battery parameter identification, published at CBMAG 2024.",
                body_pt=(
                    "Projeto acadêmico da UFSC de identificação de parâmetros de um modelo simplificado de "
                    "baterias de lítio a partir de ensaios de laboratório, com os resultados publicados como "
                    "'Levantamento de um Modelo Simplificado de Baterias de Lítio em Laboratório' no CBMAG 2024."
                ),
                body_en=(
                    "UFSC academic project identifying the parameters of a simplified lithium-ion battery model "
                    "from lab experiments, with results published as 'Experimental Identification of a "
                    "Simplified Lithium-Ion Battery Model' at CBMAG 2024."
                ),
                institution=ufsc,
                role_pt="Projeto acadêmico",
                role_en="Academic project",
                period_start="2023",
                period_end="2024",
                tools="Python, system identification, laboratory testing",
                icon="ti-battery-2",
                order=11,
            ),
            dict(
                slug="invest-jr-financial-tooling",
                title_pt="Automação de planilhas e dashboards financeiros",
                title_en="Financial spreadsheet and dashboard automation",
                summary_pt="Ferramentas de análise financeira e gestão empresarial para clientes da Invest Jr.",
                summary_en="Financial analysis and business-management tooling for Invest Jr. clients.",
                body_pt=(
                    "Como membro da Invest Jr., produzi conteúdos didáticos sobre Excel, Power Query e VBA, "
                    "conduzi workshops de investimentos e finanças pessoais, e desenvolvi planilhas automatizadas, "
                    "dashboards e ferramentas de relatórios para otimizar o acompanhamento financeiro e a tomada "
                    "de decisão dos clientes."
                ),
                body_en=(
                    "As a member of Invest Jr., I produced instructional content on Excel, Power Query, and VBA, "
                    "led workshops on investments and personal finance, and developed automated spreadsheet "
                    "systems, dashboards, and reporting tools to optimize financial tracking and decision-making "
                    "for clients."
                ),
                institution=invest,
                role_pt="Membro",
                role_en="Member",
                period_start="2020-09",
                period_end="2021-06",
                tools="Excel, Power Query, VBA",
                icon="ti-file-spreadsheet",
                order=12,
            ),
        ]

        for data in projects:
            slug = data.pop("slug")
            Project.objects.update_or_create(slug=slug, defaults=data)

    def seed_publications(self):
        data = [
            dict(
                title="Small Object Detection in Drone-Captured Images for Maritime Surveillance",
                authors="Bruno Mingoti, et al.",
                venue="SIBGRAPI",
                year=2025,
                type="paper",
                url="https://scholar.google.com.br/citations?user=Dx-d55AAAAAJ&hl=pt-BR",
                summary_pt="Modelos de detecção de pequenos objetos em imagens de drone para vigilância marítima e apoio a buscas e salvamentos.",
                summary_en="Small object detection models over drone imagery for maritime surveillance and search-and-rescue support.",
                order=1,
            ),
            dict(
                title="Filtered backprojection combined with deep learning-based sinogram denoising for improved industrial CT reconstruction",
                authors="Bruno Mingoti",
                venue="UFSC / RWTH Aachen — Trabalho de Conclusão de Curso",
                year=2025,
                type="thesis",
                url="https://scholar.google.com.br/citations?user=Dx-d55AAAAAJ&hl=pt-BR",
                summary_pt="TCC sobre reconstrução de CT industrial combinando backprojection filtrada com denoising por deep learning.",
                summary_en="Bachelor's thesis on industrial CT reconstruction combining filtered backprojection with deep learning-based denoising.",
                order=2,
            ),
            dict(
                title="Levantamento de um Modelo Simplificado de Baterias de Lítio em Laboratório",
                authors="Bruno Mingoti, et al.",
                venue="CBMAG",
                year=2024,
                type="paper",
                url="https://scholar.google.com.br/citations?user=Dx-d55AAAAAJ&hl=pt-BR",
                summary_pt="Identificação experimental de parâmetros de um modelo simplificado de baterias de lítio.",
                summary_en="Experimental identification of the parameters of a simplified lithium-ion battery model.",
                order=3,
            ),
            dict(
                title="Automated Data Stream Management Software-Stack",
                authors="Matthias Bodenbenner, Bruno Mingoti, Kilian Leonard Geiger, Robert Schmitt",
                venue="Zenodo (código aberto, projeto AMalytik)",
                year=2026,
                type="report",
                url="https://zenodo.org/records/18255616",
                summary_pt="Software-stack para gerenciamento automatizado de fluxos de dados de sensores, com matching de dispositivos, produtores e consumidores.",
                summary_en="Software stack for automated sensor data-stream management, with device/producer/consumer matching.",
                order=4,
            ),
            dict(
                title="DCC Generator and Validator Webpage",
                authors="Bruno Mingoti, Matthias Bodenbenner, Kilian Leonard Geiger, Robert Schmitt (supervisor)",
                venue="Zenodo (código aberto, projeto AMalytik)",
                year=2026,
                type="report",
                url="https://zenodo.org/records/18241584",
                summary_pt="Geração e validação de Certificados Digitais de Calibração (DCC) em XML, conforme schema da PTB.",
                summary_en="Generation and validation of Digital Calibration Certificate (DCC) XML files, following the PTB schema.",
                order=5,
            ),
        ]
        for item in data:
            Publication.objects.update_or_create(title=item["title"], defaults=item)

    def seed_experience(self):
        data = [
            dict(
                organization="Werkzeugmaschinenlabor WZL der RWTH Aachen",
                location="Aachen, Alemanha / Germany",
                role_pt="Assistente de Pesquisa (Hilfswissenschaftler — HiWi)",
                role_en="Student Assistant (Hilfswissenschaftler — HiWi)",
                period_start="2024-08",
                period_end="2025-12",
                context_pt="Instituto líder em pesquisa de máquinas-ferramenta e engenharia de produção.",
                context_en="Leading research institute on machine tools and production engineering.",
                highlights_pt=[
                    "TCC sobre backprojection filtrada com denoising de sinogramas por deep learning para reconstrução de CT industrial; duas pipelines aceleradas por GPU, com benchmark contra o software do instituto.",
                    "Serviços backend e frontend para gerenciamento automatizado de fluxos de dados (matching de dispositivos/produtores/consumidores).",
                    "Operações de banco de dados para armazenamento e assinatura digital de conjuntos de medição para Certificados Digitais de Calibração (DCC).",
                    "Suporte a projetos de metrologia industrial: medições ópticas, análises e relatórios.",
                    "Apoio na organização do 3DMC, principal evento europeu de metrologia.",
                ],
                highlights_en=[
                    "Bachelor's thesis on filtered backprojection combined with deep learning-based sinogram denoising for industrial CT reconstruction; two GPU-accelerated pipelines benchmarked against the institute's software.",
                    "Backend and frontend services for automated data-stream management (device/producer/consumer matching).",
                    "Database operations for storing and digitally signing measurement datasets for Digital Calibration Certificates (DCC).",
                    "Support for industrial metrology projects: optical measurements, analysis, and reporting.",
                    "Assistance hosting the 3DMC, Europe's leading metrology event.",
                ],
                tools="Python, TypeScript, PyTorch, GPU computing, REST APIs, digital signatures",
                order=1,
            ),
            dict(
                organization="Fundação CERTI",
                location="Florianópolis, Brasil / Brazil",
                role_pt="Estagiário cooperado — Programa NEO Empresarial",
                role_en="Co-op student — NEO Empresarial program",
                period_start="2022-03",
                period_end="2024-07",
                context_pt="Programa de formação técnica em parceria com WEG S.A., Embraco/Nidec e Landis+Gyr AG.",
                context_en="Technical training program in partnership with WEG S.A., Embraco/Nidec, and Landis+Gyr AG.",
                highlights_pt=[
                    "Pesquisa em métodos de IA para few-shot learning.",
                    "Firmware STM32 (C) para cálculos de disjuntores de caixa moldada e comunicação I2C/SPI para a WEG.",
                    "Sistema de detecção de falhas em notebooks com YOLO para a Lenovo.",
                    "Aplicação supervisória Electron + Modbus para alívio de tensões térmicas na caldeiraria da WEG (~R$ 250 mil/ano de economia).",
                    "Automação de relatórios de espectro de vibração implantada em produção.",
                    "Modelos de detecção e rastreamento de objetos em imagens aéreas marítimas para busca e salvamento (cooperação Brasil-Suécia).",
                    "Instrutor no programa interno de treinamento em ciência de dados para novos membros.",
                ],
                highlights_en=[
                    "Research on few-shot learning AI methods.",
                    "STM32 (C) firmware for molded-case circuit breaker calculations and I2C/SPI communication for WEG.",
                    "YOLO-based laptop defect detection system for Lenovo.",
                    "Electron + Modbus supervisory application for thermal stress relief in WEG's boiler area (~€40k/year savings).",
                    "Vibration-spectrum reporting automation deployed to production.",
                    "Object detection and tracking models over aerial maritime imagery for search and rescue (Brazil-Sweden cooperation).",
                    "Instructor in the team's internal data science training program for new members.",
                ],
                tools="Python, C, STM32CubeIDE, YOLO, Electron, Modbus",
                order=2,
            ),
            dict(
                organization="Invest Jr.",
                location="Florianópolis, Brasil / Brazil (remoto/remote)",
                role_pt="Membro",
                role_en="Member",
                period_start="2020-09",
                period_end="2021-06",
                context_pt="Organização sem fins lucrativos gerida por estudantes.",
                context_en="Nonprofit organization managed by students.",
                highlights_pt=[
                    "Planejamento e execução de treinamentos técnicos e soluções digitais para análise financeira e gestão empresarial.",
                    "Produção de conteúdos didáticos sobre Excel, Power Query e VBA; condução de workshops de investimentos e finanças pessoais.",
                    "Desenvolvimento de planilhas automatizadas, dashboards e ferramentas de relatórios.",
                ],
                highlights_en=[
                    "Planned and delivered technical training and digital solutions for financial analysis and business management.",
                    "Produced instructional content on Excel, Power Query, and VBA; led workshops on investments and personal finance.",
                    "Developed automated spreadsheet systems, dashboards, and reporting tools.",
                ],
                tools="Excel, Power Query, VBA",
                order=3,
            ),
        ]
        for item in data:
            ExperienceEntry.objects.update_or_create(
                organization=item["organization"], period_start=item["period_start"], defaults=item
            )

    def seed_education(self):
        data = [
            dict(
                institution="RWTH Aachen University",
                location="Aachen, Alemanha / Germany",
                degree_pt="B.Sc. Engenharia Mecânica — Intercâmbio",
                degree_en="B.Sc. Mechanical Engineering — Exchange student",
                period_start="2024-08",
                period_end="2025-12",
                details_pt=["Assistente de Pesquisa / Hilfswissenschaftler na Werkzeugmaschinenlabor WZL."],
                details_en=["Student Assistant / Hilfswissenschaftler at Werkzeugmaschinenlabor WZL."],
                order=1,
            ),
            dict(
                institution="Universidade Federal de Santa Catarina (UFSC)",
                location="Florianópolis, Brasil / Brazil",
                degree_pt="B.Sc. Engenharia Elétrica (IAA 8,91/10,0)",
                degree_en="B.Sc. Electrical Engineering (GPA 8.91/10.0)",
                period_start="2020-08",
                period_end="2027-07",
                details_pt=[
                    "Disciplinas relevantes: machine learning, estatística, cálculo avançado, processamento de imagens e álgebra linear.",
                    "Projetos: identificação de parâmetros de bateria de lítio; classificação de células de leucemia linfoblástica aguda; segmentação e estimativa de células em tecidos H&E.",
                ],
                details_en=[
                    "Relevant courses: machine learning, statistics, advanced calculus, image processing, and linear algebra.",
                    "Projects: lithium battery parameter identification; acute lymphoblastic leukemia cell classification; H&E tissue cell segmentation and estimation.",
                ],
                order=2,
            ),
        ]
        for item in data:
            EducationEntry.objects.update_or_create(
                institution=item["institution"], period_start=item["period_start"], defaults=item
            )
