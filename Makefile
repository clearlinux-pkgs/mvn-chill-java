PKG_NAME := mvn-chill-java
URL = https://github.com/twitter/chill/archive/v0.9.3.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/com/twitter/chill-java/0.9.3/chill-java-0.9.3.jar : https://repo1.maven.org/maven2/com/twitter/chill-java/0.9.3/chill-java-0.9.3.pom : https://repo.maven.apache.org/maven2/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.jar : https://repo.maven.apache.org/maven2/com/twitter/chill_2.12/0.9.3/chill_2.12-0.9.3.pom : 

include ../common/Makefile.common
