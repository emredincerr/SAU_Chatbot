TR

Bu proje, Sakarya Üniversitesi Yönetim Bilişim Sistemleri (YBS) öğrencilerine, kariyer hedefleri doğrultusunda seçmeli ders önerileri sunan bir yapay zeka destekli sistemdir. Uygulama, öğrencinin kariyer hedeflerini anlamak için metin tabanlı sorguları analiz eder ve üniversite ders kataloğundan en uygun seçmeli dersleri belirler.

Proje, Streamlit kullanılarak geliştirilmiş ve metin temelli öneriler için LangChain çatısını entegre etmiştir. Açık kaynaklı bir dil modeli olan "gemma-2-2b-it-GGUF" kullanılarak çalışmaktadır ve embedding işlemleri için "all-mpnet-base-v2" modeli kullanılmıştır. OpenAI modelleri bu projede yer almamış, yalnızca LangChain’in sunduğu altyapısal avantajlardan faydalanılmıştır.

Sistem, RAG (Retrieval-Augmented Generation) mimarisi ile çalışarak öğrenci sorgularını analiz eder, üniversite ders içeriklerinden bağlama uygun bilgileri çıkarır ve detaylı ders önerileri sunar. Bu sayede, öğrencilerin kariyer hedeflerine ulaşmak için akademik olarak en uygun seçimleri yapmalarına yardımcı olur.

NOT: Yerel modeli çalıştırabilmek için LM Studio aracılığıyla ilgili modelin yüklenmesi ve sunucunun başlatılması gerekmektedir. Bu işlem tamamlandıktan sonra uygulama, modele bağlanarak öneri süreçlerini gerçekleştirebilir.

EN

This project is an AI-powered system designed to provide elective course recommendations to students in the Management Information Systems (MIS) department at Sakarya University, based on their career goals. The application analyzes text-based queries to understand students’ career aspirations and identifies the most suitable elective courses from the university’s course catalog.

The project is built using Streamlit and integrates the LangChain framework for text-based recommendations. It operates with the open-source language model "gemma-2-2b-it-GGUF" and uses the "all-mpnet-base-v2" model for embedding tasks. OpenAI models are not utilized in this project; instead, only the infrastructural advantages provided by LangChain are employed.

The system works with a RAG (Retrieval-Augmented Generation) architecture to analyze student queries, extract contextually relevant information from the university's course content, and deliver detailed course suggestions. This helps students make the most suitable academic choices to achieve their career goals.

Note: To run the local model, it is necessary to load the model using LM Studio and start the server. Once the server is running, the application can connect to the model and perform recommendation processes.

![2](https://github.com/user-attachments/assets/0bd71241-0c66-4e84-b3a5-eb56b16fad72)

![3](https://github.com/user-attachments/assets/34e297c7-5209-46c9-bc02-ae5cf8e4808e)

![4](https://github.com/user-attachments/assets/8d8390b0-e21b-4af8-b8fc-fb3ef28ea991)

![7](https://github.com/user-attachments/assets/97191605-bc26-4fcc-b22f-c741e1437fd7)

![10](https://github.com/user-attachments/assets/04f889b6-ee5b-4207-8a49-89ddd5035fb1)

![11](https://github.com/user-attachments/assets/2695f1ef-7b69-4af7-8138-f6284a9db895)




