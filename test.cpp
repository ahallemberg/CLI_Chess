#include <iostream>
#include <string> 

class Test {
    public: 
    std::string e; 
    Test() {
        this->e = "Dette er en test";
    }; 

    Test* self(void) {
        return this;
    };
    

}; 

int main(void) {
    Test* test1 = new Test(); 
    Test* selfPtr = test1->self(); 

    std::cout << selfPtr->e << std::endl; // Output the string stored in the object
    delete test1; 
    return 0;
}