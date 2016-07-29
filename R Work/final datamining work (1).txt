 
 install package (xlsx,readxl,rpart)

 setwd("C:\\Users\\FATEMEH\\Desktop")
 getwd()
 require(readxl)
   
 mother=read_excel("Final Dataset 3_ latest.xlsx",sheet=1)
   
  mother_sub=subset(mother[1:157,]) 

   #data reduction:remove first column#

   mother=mother_sub[,-1] 
 dim(mother)
 
 #compute the correlation using chi.square for nominal attributes ,significant level alpha=0.05 #

  chisq.test(mother[,5],mother[,6])
 chisq.test(mother[,5],mother[,7])
 chisq.test(mother[,5],mother[,8])
 chisq.test(mother[,5],mother[,9])
 chisq.test(mother[,6],mother[,7])
 chisq.test(mother[,6],mother[,8])
 chisq.test(mother[,6],mother[,9])
 chisq.test(mother[,7],mother[,8])
 chisq.test(mother[,7],mother[,9])
 chisq.test(mother[,8],mother[,9])
 
 #column 6(Software_Service) and column 9(Cloud_Platform_and_Development_Service )  are significantly correlated #

 #column 7(Cloud_Security_Service) and column 8(Cloud_Storage_Service) are significantly correlated#
 
 #remove column 8(Cloud_Storage_Service) #

   mother=mother[,-8]

 #remove column (Cloud_Platform_and_Development_Service )#

   mother=mother[,-8]

 #compute the correlation using correlation coefficient for numeric attributes #
 
 cor(mother[,1],mother[,2])

 plot(mother[,1],mother[,2],xlab="number of employee",ylab="revenue",col=20)

 cor(mother[,1],mother[,4])

 plot(mother[,1],mother[,4],xlab="number of employee",ylab="customer satisfaction")

 cor(mother[,1],mother[,8])

 plot(mother[,1],mother[,8],xlab="number of employee",ylab="price")


 cor(mother[,2],mother[,4])

 plot(mother[,2],mother[,4],xlab="revenue",ylab="customer satisfaction",col=90)

 
 cor(mother[,2],mother[,8])

 plot(mother[,2],mother[,8],xlab="revenue",ylab="price",col=20)

 cor(mother[,4],mother[,8])

 plot(mother[,4],mother[,8],xlab="customer satisfaction",ylab="price",col=90)

 


  

  #1=====================================================================
 
   #min & max standardizing (number of employee)attribute in to 2 digit range#
   #so it better fits in to the category #

      employee=mother[,1]
      mini1=min(employee)
      maxi1=max(employee)
      standard_employee=((employee-mini1)/(maxi1-mini1))*89+10
      range(standard_employee)
      mother=cbind(standard_employee,mother)
      mother=mother[,-2]
      mother
   #creating vector  #
     p=rep(1:157,1)
     q=(p-.5)/157
     w=rep(1,157)  
      
  #scatter plot and qqplot of (number of employee) attribute#
   
     plot(mother[,1],main="scatter plot of standard_employee " ,ylab="standard_employee" ) 
    
     qqplot(q,mother[,1],ylab="standard_employee",main="prcentile plot of standard_employee")
    
     qqplot(mother[,1],w,xlab="standard_employee") 
    
     par(mfrow=c(2,2))
    
     qqnorm(mother[,1],ylab="standard_employee")
    
    range(mother[,1])

  #by visualizing this plot bining in to three category is appropriate #
    **CATHEGORIZE EMPLOYEE NUMBERS** 

      dm=dim( mother)
      for (i in 1:dm[1]){

           if (mother[i,1]>=69) {mother[i,1]="high"} 
      else if (mother[i,1]>=39) {mother[i,1]="medium"}
      else if (mother[i,1]<39)  {mother[i,1]="low"}
      }
    mother
 #2========================================================================
   
  
   #min & max standardizing (revenue)attribute in to 2 digit range#
   #so it better fits in to the category #

     revenue=mother[,2]
      mini2=min(revenue)
      maxi2=max(revenue)
      standard_revenue=((revenue-mini2)/(maxi2-mini2))*89+10
      range(standard_revenue)
      mother=cbind(standard_revenue,mother)
      mother=mother[,-3]
      mother

      
  #scatter plot and qqplot of (revenue) attribute#
 
     plot(mother[,1],main="scatter plot of standard_revenue " ,ylab="standard_revenue" ) 

     qqplot(q,mother[,1],ylab="standard_revenue",main="prcentile plot of standard_revenue")
    
     qqplot(mother[,1],w,xlab="standard_revenue") 
     
     par(mfrow=c(2,2))
    
     qqnorm(mother[,1],ylab="standard_revenue")
    
    range(mother[,1])

   #by visualizing this plot bining in to three category is appropriate # 
  
  **CATHEGORIZE REVENUE**
  
 
  for (J in 1:dm[1]){

 
           if (mother[J,1]>=69) {mother[J,1]="high"} 
      else if (mother[J,1]>=39) {mother[J,1]="medium"}
      else if (mother[J,1]<39)  {mother[J,1]="low"}

   }

#3 ================================================================
  
  
   #min & max standardizing (price)attribute in to 2 digit range#
   #so it better fits in to the category #
    
      price=mother[,8]
      mini3=min(price)
      maxi3=max(price)
      standard_price=((price-mini3)/(maxi3-mini3))*89+10
      range(standard_price)
      mother=cbind(standard_price,mother)
      mother=mother[,-9]
      mother

   #scatter plot and qqplot of (price) attribute#

     plot(mother[,1],main="scatter plot of standard_price " ,ylab="standard_price" )  
     
     qqplot(q,mother[,1],ylab="standard_price",main="prcentile plot of standard_price ")
     
     qqplot(mother[,1],w,xlab="standard_price") 
     
     par(mfrow=c(2,2))
     
     qqnorm(mother[,1],ylab="standard_price")
     
     range(mother[,1])

    #by visualizing this plot bining in to three category is appropriate # 
  
   
  
   **CATHEGORIZE PRICE**

   for (j in 1:dm[1]){
    
           if (mother[j,1]>=69) {mother[j,1]="high"} 
      else if (mother[j,1]>=39) {mother[j,1]="medium"}
      else if (mother[j,1]<39)  {mother[j,1]="low"}

     }
  
 4#========================
  
     plot(mother[,5],main="scatter plot of customer_satisfaction " ,ylab="customer_satisfaction") 

     qqplot(q,mother[,5],ylab="customer_satisfaction",main="prcentile plot of customer_satisfaction ")

     qqplot(mother[,5],w,xlab="customer_satisfaction") 

     par(mfrow=c(2,2))

     qqnorm(mother[,5],ylab="customer_satisfaction")

     range(mother[,5])



  **CATHEGORIZE SATISFACTION**
 
  for (I in 1:dm[1]){

          if (mother[I,5]>=74)  {mother[I,5]="satisfy"}
     else if (mother[I,5]>=51)  {mother[I,5]="mutual"}
     else if (mother[I,5] <51)   {mother[I,5]="unhappy"}      
   }
  
 


================================
 mother1=mother
  dim(mother1)
 
 # we can repeat this section for different seed=3 #
  
  set.seed(4321)
  train=sample(1:nrow(mother1),nrow(mother1)*(1/2))
  test= -train
  trainning_data=mother1[train,]
  testing_data=mother1[test,]
 dim(testing_data)
 dim(trainning_data) 
  
  tree_model=rpart(Cloud_Provider_Company~Infrastructure_Service+Software_Service+Cloud_Security_Service+ standard_price+standard_revenue
   +standard_employee+Customer_Satisfaction, method= "class" , data=trainning_data)
  
   plot(tree_model)
   text(tree_model,pretty=0)

  #compare testing dataset with  Cloud_Provider_Company# 
  
   Cloud_Provider_Company=mother1[,4] 

   testing_provider=Cloud_Provider_Company[test] 
 
 
  #check how the model is doing using test data & how testing _data is classified by tree_model#
  
  tree_pred=predict(  tree_model,testing_data ,type="class")

  # it gave us misclassification ERROR to see if  prunning is needed #

  mean(tree_pred != testing_provider) 

  

    #confusion matrix#

  t=table(tree_pred,testing_data$Cloud_Provider_Company)
  summary(t)
  plot(t)
  # to prun the tree cross validation shows where to stop pruning#
    
   printcp(tree_model) # display the results
   plotcp(tree_model) # visualize cross-validation results
   summary(tree_model) # detailed summary of splits
  
 
  prune_model=prune(tree_model,cp=tree_model$cptable[which.min(tree_model$cptable[,"xerror"]),"CP"])

  plot(prune_model)
  text( prune_model)
  prun_tree_pred=predict(  prune_model,testing_data ,type="class")

  mean(prun_tree_pred != testing_provider)
 
  ##########
 
  #we want to predict for a single data point#

   single_datapoint49=testing_data[49,]

   single_datapoint49=single_datapoint49[,-4]

   single_datatee49_pred=predict(  tree_model,single_datapoint49,type="class")
    
   single_dataprun49_pred=predict(  prune_model,single_datapoint49 ,type="class")

   

   ## 


   single_datapoint1=trainning_data[1,]

   single_datapoint1=single_datapoint1[,-4]

   single_datatree1_pred=predict(  tree_model, single_datapoint1 ,type="class")
   
   single_dataprun1_pred=predict(  prune_model, single_datapoint1 ,type="class")

   

 

   


