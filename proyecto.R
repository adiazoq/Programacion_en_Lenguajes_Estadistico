library(readxl)
library(ggplot2)
library(dplyr)

Exportaciones <- read_excel("C:/Users/ACER/Dropbox/PC/Downloads/Exportaciones.xlsx", 
                            sheet = "1. Total_Volumen", range = "D7:E782")
View(Exportaciones)
summary(Exportaciones)


Total_Valor <- read_excel("C:/Users/ACER/Dropbox/PC/Downloads/Exportaciones.xlsx", 
                            sheet = "2. Total_Valor", range = "D7:E782")
summary(Total_Valor)

#Promedios y desviaciones eśtandar por decadadas.

Exportaciones$MES <- as.Date(Exportaciones$MES)
d1=Exportaciones %>% filter(Exportaciones$MES>"1958-01-01" & Exportaciones$MES<"1968-12-01")
mean(d1$`Total Exportaciones`)
sd(d1$`Total Exportaciones`)

d2=Exportaciones %>% filter(Exportaciones$MES>"1968-01-01" & Exportaciones$MES<"1978-12-01")
mean(d2$`Total Exportaciones`)
sd(d2$`Total Exportaciones`)

d3=Exportaciones %>% filter(Exportaciones$MES>"1978-01-01" & Exportaciones$MES<"1988-12-01")
mean(d3$`Total Exportaciones`)
sd(d3$`Total Exportaciones`)

d4=Exportaciones %>% filter(Exportaciones$MES>"1988-01-01" & Exportaciones$MES<"1998-12-01")
mean(d4$`Total Exportaciones`)
sd(d4$`Total Exportaciones`)

d5=Exportaciones %>% filter(Exportaciones$MES>"1998-01-01" & Exportaciones$MES<"2008-12-01")
mean(d5$`Total Exportaciones`)
sd(d5$`Total Exportaciones`)

d6=Exportaciones %>% filter(Exportaciones$MES>"2008-01-01" & Exportaciones$MES<"2018-12-01")
mean(d6$`Total Exportaciones`)
sd(d6$`Total Exportaciones`)

d7=Exportaciones %>% filter(Exportaciones$MES>"2018-01-01" & Exportaciones$MES<"2022-07-01")
mean(d7$`Total Exportaciones`)
sd(d7$`Total Exportaciones`)

#Gŕaficas de las variaciones de precio o produccion a traves del tiempo

vec1 <- c(mean(d1$`Total Exportaciones`),mean(d2$`Total Exportaciones`),mean(d3$`Total Exportaciones`),mean(d4$`Total Exportaciones`),mean(d5$`Total Exportaciones`),mean(d6$`Total Exportaciones`),mean(d7$`Total Exportaciones`))
vec2 <- c(1958,1968,1978,1988,1998,2008,2018)
plot(vec2,vec1,main = "Grafica", col="red",xlab="Decadas",ylab="Produccion")

#Pruebas estadısticas para comparar las medias de dos decadas

t.test(d4$`Total Exportaciones`, d6$`Total Exportaciones`,
       alternative = "two.sided") 

#Diagrama de dispersión y correlaciones

regresion <- lm(Exportaciones$`Total Exportaciones` ~ Total_Valor$`Valor Nominal*`)
plot(Exportaciones$`Total Exportaciones`~Total_Valor$`Valor Nominal*`,main = "Diagrama de dispersion",xlab ="Valor Nominal",ylab = "Total Exportaciones") 
abline(regresion, col="red", lwd=2)

cor(Exportaciones$`Total Exportaciones`,Total_Valor$`Valor Nominal*`)



