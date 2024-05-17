import pandas as pd
import ydata_profiling


df = pd.read_csv("Crop_recommendation.csv")   #读取数据集

df = pd.get_dummies(df)    #使用独热编码
df.to_csv('Process_crop_recommendation.csv',index=False)   #将独热编码后的数据集输出为文件Process_crop_recommendation.csv
.css-button-arrow--blue {
  min-width: 130px;
  height: 40px;
  color: #fff;
  padding: 5px 10px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  outline: none;
  overflow: hidden;
  border-radius: 5px;
  border: none;
  background-color: #3d348b
}
.css-button-arrow--blue:hover {
  border-radius: 5px;
  padding-right: 24px;
  padding-left:8px;
}
.css-button-arrow--blue:hover:after {
  opacity: 1;
  right: 10px;
}
.css-button-arrow--blue:after {
  content: "\00BB";
  position: absolute;
  opacity: 0;
  font-size: 20px;
  line-height: 40px;
  top: 0;
  right: -20px;
  transition: 0.4s;
}