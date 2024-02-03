install.packages('Tmisc')

library(Tmisc)
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>% 
  summarise(mean(x),sd(x),mean(y),sd(y),cor(x,y))



ggplot(quartet,aes(x,y))+geom_point() + geom_smooth(method = lm,se= FALSE)+ facet_wrap(~set)


install.packages('datasauRus')
library('datasauRus')

ggplot(datasaurus_dozen,aes(x=x,y=y,colour=dataset))+geom_point()+theme_void()+theme(legend.position = "none")+facet_wrap(~dataset,ncol=3)

install.packages('SimDesign')
library(SimDesign)

actual_temp <- c(68.3,70,72.4,71,67,70)
predicted_temp <- c(67.9,69,71.5,70,67,69)
bias(actual_temp,predicted_temp)

actual_sales <- c(150,206,137,247,116,287)
predicted_sales <-  c(200,300,150,250,150,300)
bias(actual_sales,predicted_sales)

colnames(quartet)


ggplot(data= penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g),color='purple')+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g),color='purple')

ggplot(data = penguins)+
  geom_smooth(mapping = aes(x=flipper_length_mm,y=body_mass_g,linetype=),color='purple')
  
ggplot(data = penguins)+
  geom_jitter(mapping = aes(x=flipper_length_mm,y=body_mass_g))



ggplot(data=diamonds)+
  geom_bar(mapping = aes(x=cut,fill=clarity))+
  facet_wrap(~cut)


ggplot(data=penguins)+
  geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  labs(title = 'Penguinsssss',subtitle = 'yisss',
    caption='data collected.. (im at the bottom)')+
  annotate('text',x=220,y=3500,label='the gentoos are huge',color='red',fontface ='bold', size=12,angle=25)
 


install.packages('rmarkdown')

library(rmarkdown)

