curl -v -H "app_id:6667e13f" -H "app_key:a5d5074a84da848f6fab9f0a021a0b93" -X POST "http://api.kairos.io/gallery/view" -d '{"gallery_name":"Kremer"}'

curl -v -H "app_id:6667e13f" -H "app_key:a5d5074a84da848f6fab9f0a021a0b93" -X POST "http://api.kairos.io/gallery/remove_subject" -d '{"gallery_name":"Kremer","subject_id":"Ben"}'

curl -v -H "app_id:6667e13f" -H "app_key:a5d5074a84da848f6fab9f0a021a0b93" -X POST "http://api.kairos.io/gallery/list_all"




a5d5074a84da848f6fab9f0a021a0b93




curl -v -H "app_id:6667e13f" -H "app_key:a5d5074a84da848f6fab9f0a021a0b93" -X POST "http://api.kairos.io/detect" -d '{"url":"http://dev.kremerdesign.com/twin_study/images/3.jpg"},"selector":"FULL"}'


curl -v -H "app_id:6667e13f" -H "app_key:a5d5074a84da848f6fab9f0a021a0b93" -X POST "http://api.kairos.io/recognize" -d '{"url":"http://dev.kremerdesign.com/twin_study/images/3.jpg","gallery_name":"Kremer","threshold":".2","max_num_results":"15"}'