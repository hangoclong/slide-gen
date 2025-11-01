<!-- image -->

- After reading
- this briefing, you will be
- able to do the
- following:

<!-- image -->

## Foundations of Information Systems Infrastructure

1.  Discuss foundational information systems (IS) hardware concepts.
2.  Describe foundational topics related to system software, programming languages, and application development environments.
3.  Describe foundational networking and internet concepts.
4.  Explain foundational database management concepts.

In Chapter 3, 'Managing the Information Systems Infrastructure and Services,' you learned about the key components of a comprehensive information systems (IS) infrastructure and why its careful management is necessary. This Technology Briefing will expand that discussion, providing you with a deeper understanding of those topics. Each of the major sections within this briefing provides optional material that stands alone from the other sections as well as the entire book. Likewise, the end-of-chapter material is presented in separate sections to facilitate this independence.

## Foundational Topics in IS Hardware

IS hardware is an integral part of the IS infrastructure and is broadly classified into three types: input, processing, and output technologies. In this section, we examine foundational topics related to IS hardware.

## Input Technologies

Input technologies are  used to enter data into a computer, laptop, tablet, or smartphone (see Figure TB1). Widely used input devices include various types of keyboards or pointing devices like track pads, graphics tablets, and mice. Other, more specialized input devices include biometric fingerprint readers to identify or authenticate people (for access control, such as for computers, smartphones or secure laboratories, or for border controls; see Chapter 10, 'Securing Information Systems'), radio frequency identification (RFID) scanners to track valuable inventory in a warehouse (see Chapter 8, 'Strengthening Business-to-Business Relationships via Supply Chain and Customer Relationship Management'), and eye-tracking devices, used primarily by the disabled for help with operating computers as well as for usability studies and scientific research studies. Likewise, Internet of Things (IoT) sensors are used to capture massive amounts of data about a device or environmental condition, such as temperature, humidity, acceleration, or direction.

ENTERING BATCH DATA. Large amounts of routine data, referred to as batch data , are often entered into the computer using scanners that convert printed or handwritten text and images into digital data. Scanners range from small handheld devices to large desktop boxes that resemble personal photocopiers. Rather than duplicating the image on another piece of paper, the computer translates the image into digital data that can be stored or manipulated by the computer. Insurance companies, universities, and other organizations that routinely process large numbers of forms and documents are typically using scanner technology to increase employee productivity; entering a large number of separate forms or documents into a computer system and then manipulating these data at a single time is referred to as batch processing .

Once a document is converted into digital format, text recognition software uses optical character recognition to  convert  typed,  printed,  or  handwritten  text  into  the  computer-based characters that form the original letters and words. Other special-purpose scanning technologies include optical mark recognition devices, bar code readers , and magnetic ink character recognition , as summarized in Table TB1.

<!-- image -->

## FIGURE TB1

All computing devices utilize input technologies.

Source: HNK/Shutterstock.

## TABLE TB1 Specialized Scanners for Inputting Data

| Scanner                            | Description                                                                                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Optical mark recognition           | Used to scan questionnaires and test answer forms ('bubble sheets') where answer choices are marked by filling in circles using pencil or pen                                                                                   |
| Optical character recognition      | Used to read and digitize typewritten, computer-printed, and even handwrit- ten characters such as product specifications on sales tags on department store merchandise, patient data in hospitals, or addresses on postal mail |
| Bar code reader                    | Used mostly in grocery stores and other retail businesses to read bar code data at the checkout counter; also used by libraries, banks, hospitals, utility companies, etc.                                                      |
| Magnetic ink character recognition | Used by the banking industry to read data, account numbers, bank codes, and check numbers on preprinted checks                                                                                                                  |
| Biometric scanner                  | Used to scan human body characteristics of users to enable everything from access control to payment authorization                                                                                                              |

Other Input Technologies Smart cards are special credit card-sized cards containing a microprocessor chip, memory circuits, and often a magnetic stripe. Smart cards can be used for various applications, including identification, providing building access, or making payments (e.g., at vending machines or checkout counters). Some smart cards allow for contactless transmission of data using RFID technology (e.g., MasterCard Contactless or Visa payWave). Like RFID technology, near-field communication (NFC) is used in smartcards or mobile phones to enable contactless transmission of data. Biometric devices, discussed in more detail in Chapter 10, are being used primarily for identification and authentication purposes. These devices read certain body features, including irises, fingerprints, and hand or face geometry, and compare them with stored profiles. Biometric devices are now also being included in consumer products such as laptops, computer keyboards, or mobile devices, allowing users to log on to the device by scanning their fingerprints rather than typing their usernames and passwords. Further, most modern smartphones use various sensors to obtain data about the device's location (global positioning system [GPS] sensor), orientation (compass and gyroscope), acceleration (accelerometer), altitude (barometer), proximity to the user's body, or ambient light. Likewise, the various Internet of Things (IoT) devices have become another important input technology. Entrepreneurs and established companies around the globe are using a variety of sensors to collect diverse types of data to automate processes or provide innovative services to customers, from monitoring newborn babies, to providing reminders for taking medication, fitness tracking, home automation, and countless other uses (see Table TB2 for the most commonly used types of IoT sensors).

ENTERING AUDIO AND VIDEO. When entering audio (i.e., sound) or video (i.e., still and moving images) data into a computer, the data must be digitized before they can be manipulated, stored, and played or displayed. In addition to the manipulation of music, audio input is helpful for operating a computer when a user's hands need to be free to do other tasks. Video input is used for assisting in security-related applications, such as room monitoring and employee verification, as well as for videoconferencing and chatting on the internet, using a PC and a webcam.

Voice Input Voice data are input into a computer system using microphones. A process called speech recognition also makes it possible for your computer or smartphone to understand speech. Voice-to-text software is an application that uses a microphone to monitor a person's speech and then converts the speech into text. Speech recognition technology can also be especially helpful for disabled computer users, physicians and other medical professionals, airplane pilots, factory workers whose hands get too dirty to use keyboards, mobile users who don't want to type while walking or driving, and computer users who cannot type and do not want to learn. Increasingly, interactive voice response (IVR) , based on speech recognition technology, is used for telephone surveys or to guide you through the various menu options when calling a company's customer service line. Advances in artificial intelligence (AI) have

## TABLE TB2 IoT Sensors

| Type             | Sample applications                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Temperature      | Refrigeration, air conditioning, manufacturing, agricultural, healthcare                                                   |
| Proximity        | Retail, automotive, lighting, security, smartphone                                                                         |
| Pressure         | Manufacturing, water system, heating, automotive, smartphones                                                              |
| Water quality    | Water distribution (measure chlorine, pH, conductivity, turbidity, etc.)                                                   |
| Chemical         | Industrial safety, pharma, laboratories, recycling                                                                         |
| Gas              | Manufacturing, chemical industries, oil &gas, agriculture, healthcare, automotive (breatha- lyzer), air quality monitoring |
| Smoke            | Manufacturing, healthcare, HVAC, building safety                                                                           |
| Infrared         | Healthcare, home appliances, wearables, optical communication, automotive                                                  |
| Level            | Fuel gauge, tsunami warnings, medical equipment, beverage processing                                                       |
| Image            | Digital cameras, biometrics, night vision, radar, healthcare                                                               |
| Motion detection | Security, appliances, energy management systems, automated parking systems, smart city                                     |
| Accelerometer    | Smartphones, anti-theft, aircraft, automotive, consumer electronics, athlete monitoring                                    |
| Gyroscope        | Car navigation, game controllers, robotics control, drone control                                                          |
| Humidity         | Agriculture, manufacturing, HVAC, museums, meteorology, medical                                                            |
| Optical          | Healthcare, pharmaceutical, energy, aerospace, environment monitoring                                                      |
| Acoustic         | Smart city, healthcare, fish detection, security, monitoring machine health                                                |

Source: Based on Sharma (2020).

made voice input a viable way of interacting with a variety of devices, ranging from the voice enabled assistants in your smart phones to smart speakers in your home.

Other Forms of Audio Input In addition to using a microphone, users can enter audio using electronic keyboards, or they can transfer audio from another device (such as an audio recorder, a digital media player, or a smartphone). The users can then analyze and manipulate the sounds via sound editing software, output the sounds to speakers, or store the digitized sounds to MP3 or other file formats.

Video Input Video data can be entered into a computer using digital cameras that record still images or video clips in digital form on small, removable memory cards. File size is primarily influenced by the resolution, compression, and file format you select for pictures or the length of the recording for video. As webcams (as well as cameras integrated into mobile devices) have become very popular with people wanting to use the internet for chatting with friends and family using programs like Skype, Google Hangouts, or FaceTime, protocols to transmit data in a continuous fashion are used. In contrast to discrete audio or video files that must be completely downloaded before they can be opened, streaming audio and streaming video (together referred to as streaming media ) are data streams transmitted using specific protocols that are available for immediate playback on the recipient's device. Similarly, the video-sharing site YouTube, online radio stations, and Netflix use specific protocols to stream media content.

## Processing: Transforming Inputs into Outputs

In this section we provide a brief overview of computer processing. Processing technologies , contained  inside  any  computing  device  (including  smartphones,  tablets,  or  wireless  routers), transform inputs into outputs.

## FIGURE TB2

A computer's motherboard holds or connects to all of the computer's electronic components.

Source: Bretislav Horak/Shutterstock.

## FIGURE TB3

A CPU performs all operations of a computer.

Source: Tatiana Popova/Shutterstock.

<!-- image -->

HOW A COMPUTER WORKS. Inside any computing device, you will find the motherboard , a plastic or fiberglass circuit board that holds or connects to all of the computer's electronic components (see Figure TB2). The motherboard holds the central processing unit (CPU) , or microprocessor , which is the main component of a computing device, and connects it to the power supply and primary and secondary storage as well as to various peripherals (such as input and output devices or expansion cards, such as dedicated sound or video cards). The CPU is often called the computer's brain, as it is responsible for performing all the operations of the computer (see Figure TB3). Its job includes loading the operating system (e.g., Windows 10, macOS, or Ubuntu Linux) when the machine is first turned on and performing, coordinating, and managing all the calculations and instructions relayed to it while the computer is running. The CPU, a small device made of silicon, is composed of millions of tiny transistors arranged in complex patterns that allow it to interpret and manipulate data. In addition to the number of transistors on the CPU, three other factors greatly influence its speed-its system clock speed (the number of instructions a CPU can execute in a fixed amount of time), registers, and cache memory (described later). The CPU consists of two main sections: the arithmetic logic unit (ALU) and the control unit , together often referred to as its core. The ALU performs calculations and logical operations, which involve comparing packets of data and then executing appropriate instructions. Combined in various ways, these functions allow the computer to perform complicated operations rapidly. The control unit works closely with the ALU, fetching and decoding instructions as well as

<!-- image -->

retrieving and storing data. Many modern CPUs have more than one set of ALU and control units on a single chip and are referred to as multi-core processors . Multi-core processers can divide processing operations into independent streams that are performed in parallel by the separate cores, greatly speeding up the performance of the CPU.

Inside all computers, data are represented in the form of binary digits, or bits (i.e., the 0s and 1s a computer understands); a sequence of 8 bits is referred to as a byte . Different binary codes have been developed to represent characters or numbers as strings of bits. A widely used standard is the American Standard Code for Information Interchange (ASCII) , where, for example, the binary digits '01100001' represent the letter a . Due to limitations in the number of characters that can be represented, as well as for specialized applications, various other codes have been developed. For example, Unicode has gained widespread acceptance, as it allows for representing characters and scripts beyond the Latin alphabet, including traditional and simplified Chinese, Cyrillic, Hebrew, and Arabic. Any input your computer receives (say, a keystroke or mouse movement) is digitized , or translated into binary code, and then processed by the CPU.

Within the computer, an electronic circuit generates pulses at a rapid rate, setting the pace for processing events to take place, just like a metronome marks time for a musician. This circuit is called the system clock . A single pulse is a clock tick , and a fixed number of clock ticks is  required to execute a single instruction. In microcomputers, the processor's clock speed is measured in hertz (Hz) or multiples thereof. One megahertz (MHz) is 1 million clock ticks, or instruction cycles, per second. Personal computer speeds are most often indicated in gigahertz (GHz, or 1 billion hertz). Microprocessor speeds improve so quickly that faster chips are on the market about every 6 months. Today, most new PCs operate at more than 3 GHz. To give you an idea of how things have changed, the original IBM PC had a clock speed of 4.77 MHz.

As its inner workings are very complex, for most of us it is easiest to think of a CPU as being a 'black box' where all the processing occurs. The CPU uses registers and cache memory (both located inside the CPU) and RAM (located outside the CPU) as primary , or temporary, storage space for data that are currently being processed. The CPU interacts with secondary storage (such as a hard drive, optical disk , or flash drive ) for permanently storing data; as primary storage is considerably faster than secondary storage, the amount of primary storage greatly influences a computer's performance. The different types of storage are discussed next.

STORAGE. A computer has various types of storage, each serving a specific purpose. The primary differences between different types of storage are capacity, volatility, and read/write speed (see Table TB3 for a comparison of different storage technologies).

TABLE TB3 Different Storage Technologies

| Name          | Volatility   | Speed           | Access     | Capacity                                         | Usage                                                                 |
|---------------|--------------|-----------------|------------|--------------------------------------------------|-----------------------------------------------------------------------|
| Register      | Volatile     | Extremely fast  | Random     | 32 or 64 bits per register                       | Data directly used by CPU                                             |
| Cache         | Volatile     | Extremely fast  | Random     | Typically up to 20MB                             | Data and instructions used by CPU                                     |
| RAM           | Volatile     | Very fast       | Random     | Depends on configuration; typically up to 128 GB | Programs and data currently used                                      |
| ROM           | Nonvolatile  | Fast            | Random     | Very low                                         | Instructions used before the operating system is loaded               |
| SSD           | Nonvolatile  | Fast            | Random     | High                                             | Storage of programs and data                                          |
| Hard drive    | Nonvolatile  | Relatively slow | Random     | High                                             | Storage of programs and data                                          |
| Optical disks | Nonvolatile  | Slow            | Random     | Medium                                           | Backup and long-term storage; software distribution; music and movies |
| Tape          | Nonvolatile  | Very slow       | Sequential | High                                             | Archiving of data                                                     |

Primary Storage Primary storage (such as random-access memory [RAM] ), also called main memory, is located on the motherboard and is used to store the data and programs currently in use; primary storage uses memory chips (consisting of transistors and capacitators) to store data. Because instructions and data stored in RAM are lost when the power to the computer is turned off, it is referred to as volatile memory . Within the CPU itself, registers provide relatively small temporary storage locations where data must reside while being processed or manipulated. For example, if two numbers are to be added together, both must reside in registers, with the result placed in a register. Consequently, the number and size of the registers can also greatly influence the speed and power of a CPU.

A cache (pronounced 'cash') is a small block of memory used by processors to store those instructions most recently or most often used. Just as you might keep file folders that you use most in a handy location on your desktop, cache memory is located within the CPU. Thanks to cache memory, before performing an operation, the processor does not have to go directly to main memory, which is slower and farther away from the microprocessor and takes longer to reach. Instead, it can check first to see if needed data are contained in the cache. Cache memory is another way computer engineers have increased processing speed.

Modern CPUs have a hierarchy of cache memory (level 1, level 2, or even level 3); the lower levels of cache memory are faster but also smaller and more expensive. The more cache available to a CPU, the better the overall system performs because more data are readily available (although at a certain size, factors such as heat emission and power consumption become prohibitive to increasing the CPU cache).

Read-only memory (ROM) is used to store programs and instructions that are automatically loaded when the computer is turned on (before the operating system is loaded), such as the basic input/output system (BIOS) . In contrast to other forms of primary storage, ROM is nonvolatile memory , which means that it retains the data when the power to the computer is shut off.

Secondary Storage Secondary storage refers to technologies for permanently storing data to a large-capacity, nonvolatile storage component, such as a hard drive (hard disk drive) . Most of the software running on a computer, including the operating system, is stored on the hard drive. Hard drives are usually installed internally, but additional hard drives may be externally located and connected via cables.

The storage capacity of the hard drives for today's microcomputers is typically measured in gigabytes (GB, billions of bytes) or terabytes (TB, trillions of bytes). It is not unusual for PCs currently on the market to come equipped with hard drives with a 1-2 TB storage capacity. Modern supercomputers can have millions of terabytes of storage. To make sure critical data are not lost, some computers employ redundant array of independent disks (RAID) technology to store redundant copies of data on two or more hard drives. RAID is not typically used on an individual's computer, but it is very common for web servers and many business systems. RAID is sometimes called a 'redundant array of inexpensive disks' because it is typically less expensive to have multiple redundant disks than fewer highly reliable and expensive ones.

A traditional hard drive consists of several magnetic disks, or platters, used for data storage (see Figure TB4). Each disk within a disk pack has an access arm with two read/write heads -one positioned close to the top surface of the disk and another positioned close to the bottom surface of the disk-to inscribe or retrieve data. When reading from or writing to the disks, the read/ write heads are constantly repositioned to the desired storage location for the data while the disks are spinning at speeds of 5,400 to 15,000 revolutions per minute. The read/write heads do not actually touch either surface of the disks. In fact, a head crash occurs if the read/write head for some reason touches the disk, leading to a loss of data. Because of the mechanical action needed to position the read/write heads, hard drives are comparably slow; it takes a permanent storage device such as a hard drive about 3-10 milliseconds to access data. Within a CPU, however, a single transistor can be changed from a 0 to a 1 in about 10 picoseconds (10-trillionths of a second). Changes inside the CPU occur about 1 billion times faster than they do in a hard drive because the CPU operates only on electronic impulses, whereas the hard drives perform both electronic and mechanical activities, such as spinning the disk and moving the read/write head. Mechanical activities are extremely slow relative to electronic activities; however, modern hard drives use cache memory to decrease the time needed to access frequently used data. A newer secondary storage technology called solid-state drive (SSD) uses nonvolatile memory chips (i.e., flash memory ) to store data; as SSDs have no moving parts, they are typically faster (with access times of 0.1-0.5

<!-- image -->

millisecond), quieter, and more reliable but also more expensive than traditional hard disk drives. Solid-state drives have become increasingly popular due to the rise of smartphones and tablets. Given their performance, weight, and reliability, they are also increasingly used for laptops and even high-performance servers and supercomputers.

Removable Storage Media There are different types of removable storage: flash memory, optical disks, and tapes. Flash memory is a memory chip-based nonvolatile computer storage method that is used in USB flash drives, solid-state hard drives, and memory cards (such as SD cards) used for storing music and pictures in digital cameras and music players. A flash drive is a data storage device that includes flash memory with an integrated USB interface. Flash drives are relatively inexpensive storage devices typically having capacities of 16-512 GB; the highestcapacity flash drives can store up to 2 TB of data.

Optical disks (i.e., disks that are written/read using laser beam technology) are very inexpensive removable nonvolatile storage media used to store data (e.g., photos and videos) and distribute software, video games, and movies. Optical disks store binary data in the form of pits and flat areas on the disk's surface (where the pits and flats represent the 0s and 1s, respectively); an optical disk drive's laser beam can then read the data based on the reflection of the disk's surface. For many years, CD-ROMs (compact disc-read-only memory) were the standard for distributing data and software because of their low cost and their storage capacity of 700 MB. As CD-ROMs cannot be written to, most computers support other types of optical disks that data can be written to, such as the CD-R (compact disc-recordable) . Whereas a CD-R can be written onto only once, a CD-RW (compact disc-rewritable) can be written onto multiple times. The DVD-ROM (digital versatile disc-read-only memory) has  more storage space than a CD-ROM because DVD-ROM (or typically referred to as simply DVD) drives use a shorter-wavelength laser beam that allows more optical pits to be deposited on the disk. Like compact discs, there are recordable (DVD-R) and rewritable (DVD-RW) versions of this storage technology. DVDs used for the distribution of movies are also called digital video discs . The increasing demand for high-definition video content led to the creation of Blu-ray, a DVD format that provides up to 50 GB of storage.

Tapes are removable, high-capacity secondary storage media; allowing only for sequential access, tapes are typically only used for archiving data and long-term storage. Tapes used for data storage consist of narrow plastic tape coated with a magnetic substance. Storage tapes are typically enclosed in a cartridge, like a music cassette, and must be inserted into a tape reader. As with other forms of magnetic storage, data are stored in tiny magnetic spots. The storage capacity of tapes is expressed as density , which equals the number of characters per inch or bytes per inch (BPI) that can be stored on the tape.

## FIGURE TB4

A hard drive consists of several disks that are stacked on top of one another and read/write heads to read and write data. Source: alias Studiot Oy/Shutterstock.

Having a life span of several decades, magnetic tape is still used for backing up or archiving large amounts of computer data, but it is gradually being replaced by high-capacity disk storage because disk storage is equally reliable. In fact, data stored on disks are easier and faster to locate because when using disks, computers do not have to scan an entire tape to find specific data.

PORTS AND POWER SUPPLY. To use the full functionality of a computer, you need to be able to connect various types of peripheral devices, such as mice, printers, and cameras, to the system unit. A port provides a hardware interface for connecting devices to computers. The characteristics of various types of ports are summarized in Table TB4. A final key component of any computing device is the power supply , which converts electricity from the wall socket to a lower voltage. Whereas typically power supplied by the utility companies can vary from 100 to 240 volts AC, depending on where you are in the world, a PC's components use lower voltages-3.3 to 12 volts DC. The power supply converts the power accordingly and regulates the voltage to eliminate spikes and surges common in most electrical systems. For added protection against external power surges, many PC owners opt to connect their systems to a separately purchased voltage surge suppressor. The power supply includes one or several fans for air cooling the electronic components inside the system unit-that low humming noise you hear while the computer is running is the fan.

Now that you understand how data are input into a computer and how data can be processed and stored, we can turn our attention to the third category of hardware-output technologies.

## Output Technologies

Output technologies , such as a computer monitor or printer, deliver information to you in a usable format, or act on the processed data (as is the case with IoT devices). A printer is an output device that produces a paper copy of alphanumeric data or other content from a computer. Printers vary in price, performance, and capabilities (e.g., document size, color or black and white, technology, speed, resolution, quality). Inkjet, LED, or laser technology is used in most personal printers.

Monitors are used to display information from a computer and, like printers, can vary in price, performance, and capabilities (e.g., screen size, color, technology, resolution, and so on). Monitors can be color, black and white, or monochrome (meaning all one color, usually green or amber). Today, monochrome monitors are used primarily in cash registers and other point-ofsale systems. Most modern monitors use liquid crystal display (LCD) technology because they

TABLE TB4 Common Computer Ports, Applications, and Descriptions

| Port Name                                                  | Used to Connect                                                                             | Description                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Serial                                                     | Modem, mouse, keyboard, terminal display, MIDI                                              | ■ Transfers one bit at a time ■ Slowest data transfer rates                                                             |
| USB                                                        | Printer, scanner, mouse, keyboard, digital camera and camcorders, external disk drives      | ■ Extremely high-speed data transfer method ■ Up to 10 Gbps using USB3.1 ■ Up to 127 devices simultaneously connected   |
| IEEE 1394 ('Fire Wire')                                    | Digital cameras and camcorders, external disk drives                                        | ■ Extremely high-speed data transfer method ■ Up to 3.2 Gbps ■ Up to 63 devices simultaneously connected                |
| Thunderbolt                                                | Simultaneous transmission of Display- Port (video and audio), PCI Express (data), and power | ■ Extremely high-speed data transfer method ■ Up to 40 Gbps ■ Up to 7 devices simultaneously connected to a single port |
| Ethernet                                                   | Network                                                                                     | ■ Most common standard for local area networks                                                                          |
| VGA (Video Graphics Array), DVI (Digital Visual Interface) | Monitors                                                                                    | ■ VGA is designed for transmission of analog video signals ■ DVI allows for transmission of digital video signals       |
| HDMI (High Definition Multi- media Interface), DisplayPort | Monitors, home theater                                                                      | ■ HDMI and DisplayPort allow for simultaneous transmis- sion of digital audio and video signals                         |

are lighter and thinner than the bulky cathode ray tubes (CRT) used in old computer displays and  televisions.  Because  display  monitors  are  embedded  into  a  broad  range  of  products  and devices, such as cell phones, digital cameras, and automobiles (e.g., to display route maps and other relevant information), they must be sturdy, reliable, lightweight, energy efficient, and low in cost. Newer display technologies, such as organic light-emitting diodes (OLED) , require far less power and are much thinner than traditional LCD panels. Finally, projectors are often used for presentation to an audience (and by many to project a large video image in a home theater).

In addition to traditional monitors, touch screen displays have become extremely popular with the development of smartphones, tablets, high-end laptops, and a variety of technology gadgets. A touch screen is a display screen that is also an input device; a user interacts with the device by touching pictures or words on the screen with a finger or a stylus. In addition to your smartphone or tablet, touch screens are used in ATMs, retail point-of-sale terminals, car navigation, and industrial control computers. Touch screens provide great flexibility in how an input device can look and operate.

Especially for mobile computing, monitor technology is still a challenge. In addition to screen size and power requirements of commonly used display technologies, glare is often an issue, and many laptop screens are hard to read in bright sunlight. Over the past decades, there has been a steady stream of enhancements related to improved resolution and reduced power consumption. It is forecasted that the next generation will be lightweight, thin, and flexible like paper, as well as inexpensive and not require external power to retain an image. Recently, manufacturers have introduced flexible glass for touch screens, which has allowed for new form factors of mobile devices.

As you have learned in Chapter 1, IoT devices are physical devices (the 'things', such as a security camera, fitness tracker, or autonomous vehicle) that are connected to the digital world. As such, the core components of IoT devices are sensors (discussed earlier), some kind of processing hardware, connectivity, and output hardware, typically in the form of actuators. Whereas sensors  are  used  to  detect  something,  actuators  (such  as  motors  or  relays)  are  used  to  effect change in the environment (e.g., by moving things, turning valves on or off, etc.). Often, IoT devices operate in a continuous loop, in that the sensors are used to detect any changes resulting from the actions effected by the actuators.

Now that you have learned more about IS hardware, we will focus on software, another key component of the IS infrastructure.

## Foundational Topics in IS Software

Software refers to programs, or sets of instructions, that allow all the hardware components in your computer system to speak to each other and to perform the desired tasks. Throughout the book, we have discussed a variety of application software, from large business systems (e.g., an enterprise resource planning system) to office automation and personal productivity tools. Without software, the biggest, fastest, most powerful computer in the world is nothing more than a fancy paperweight. Software is intertwined with all types of products and services-toys, music, appliances, healthcare, and countless other products. Here, we provide some background on this critical component to all computer-based products.

## System Software

In Chapter 3, you learned about one type of system software, the operating system, and its many different tasks. More specifically, common tasks of an operating system include the following:

- ■ Booting (or starting) your computer
- ■ Reading programs into memory and managing memory allocation
- ■ Managing where programs and files are located in secondary storage
- ■ Maintaining the structure of directories and subdirectories
- ■ Formatting disks
- ■ Controlling the computer monitor
- ■ Sending documents to the printer

Just as there are many kinds of computers, there are many different kinds of operating systems (see Table TB5). In general, operating systems-whether for large mainframe computers, desktop computers, or smartphones-perform similar operations. Obviously, large multiuser mainframes are more complex than small desktop systems; therefore, the operating system must account for and manage that complexity. However, the basic purpose of all operating systems is the same.

## TABLE TB5 Common Operating Systems

| Operating System   | Description                                                                                                                                                                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| z/OS               | A proprietary operating system developed specifically for large IBM mainframe systems.                                                                                                                                                                                   |
| Unix               | A multiuser, multitasking operating system that is available for a wide variety of computer platforms. Commonly used because of its superior security.                                                                                                                   |
| Windows            | Currently, the Windows desktop operating system is by far the most popular in the world. Variations are also used to operate large servers, tablets, and smartphones.                                                                                                    |
| macOS              | The first commercial graphical-based operating system, making its debut in 1984. The operating system of Apple computers.                                                                                                                                                |
| Linux              | An open source operating system designed in 1991 by a Finnish student. Known as a secure, low-cost, multiplatform operating system. Linux users can choose between different 'flavors' (or distributions) depending on their needs (such as the novice-friendly Ubuntu). |
| Android            | Google's Linux-based operating system for mobile devices.                                                                                                                                                                                                                |
| Ios                | Apple's mobile operating system.                                                                                                                                                                                                                                         |

A second type of system software is device drivers, which allow the computer to communicate with various hardware devices. The third major type of systems software, utilities (or utility programs ), is designed to manage computer resources and files. Some utilities are included in operating systems, while others must be obtained separately and installed on your computer. Table TB6 provides a sample of a few utility programs that are considered essential.

## Programming Languages and Development Environments

Each piece of software is developed using some programming language. A programming language is the computer language the software developer uses to write programs. For application software, such as spreadsheets, web browsers, or accounting software, the underlying programming language is invisible to the user. However, programmers in an organization's IS group, and in some instances end users, can use programming languages to develop their own specialized applications. The source code (i.e.,  the program written in a programming language) must be translated into object code-called assembly or machine language-that the hardware can understand. Normally, the source code is translated into machine language using programs called compilers and interpreters .

## TABLE TB6 Common Types of Computer Software Utilities

| Utility                       | Description                                                                                                                                                                                          |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Backup                        | Archives files from the hard drive to tapes, flash drives, or other storage devices.                                                                                                                 |
| File defragmentation          | Converts fragmented files (i.e., files not stored contiguously) on your hard drive into contiguous files that will load and be manipulated more rapidly.                                             |
| Disk and data recovery        | Allows the recovery of damaged or erased data from hard drives and flash drives.                                                                                                                     |
| Data compression              | Compresses data by substituting a short code for frequently repeated patterns of data, much like the machine shorthand used by court reporters, allowing more data to be stored on a storage medium. |
| File conversion               | Translates a file from one format to another so that it can be used by an application other than the one used to create it.                                                                          |
| Antivirus                     | Scans files for viruses and removes or quarantines any virus found.                                                                                                                                  |
| Spyware detection and removal | Scans a computer for spyware and disables or removes any spyware found.                                                                                                                              |
| Media player                  | Allows listening to music or watching video on a computer.                                                                                                                                           |

<!-- image -->

<!-- image -->

COMPILERS AND INTERPRETERS. A compiler takes an entire program's source code written in a programming language and converts it into an executable , that is, a program in machine language that can be read and executed directly by the computer (see Figure TB5). Although the compilation process can take quite some time (especially for large programs), the resulting executables run very fast; thus, programs are usually compiled before they are sold as executables to the customers. The customers purchase only the executable but do not have access to the program's source code; thus, they can run the program but not make any modifications to it.

Some programming environments do not compile the entire program into machine language. Instead, each statement of the program is converted into machine language and executed 'on the fly' (i.e., one statement at a time), as depicted in Figure TB6. The type of program that does the conversion and execution is called an interpreter . As the source code is translated each time the program is run, it is easy to quickly evaluate the effects of any changes made to the program's source code. However, this also causes interpreted programs to run much slower than compiled executables. Programming languages can be either compiled or interpreted.

PROGRAMMING LANGUAGES. Over the past few decades, software has evolved. As software has evolved, so have the programming languages. Each programming language has been designed at a particular time, for a particular use, and the first generations of programming languages were quite crude by today's standards. Some popular programming languages are listed in Table TB7.

Of course, programming languages continue to evolve, with object-oriented languages, visual programming languages, and languages for developing websites and AI applications having rapidly gained popularity. We discuss these next.

Object-Oriented Languages Object-oriented languages are extremely popular with application developers. Object-oriented languages use common modules (called objects), which combine properties and behaviors to define the relevant system components. An example of an object would be a specific student who has a name, an address, and a date of birth (i.e., the properties) but can also perform certain operations, such as register for a course (the behaviors). If an object-oriented programming language is being used, it enables the design and implementation of the objects to happen quickly and simultaneously, as oftentimes preexisting objects can be reused or adapted. For important concepts related to object-oriented languages, see Table TB8.

Visual Programming Languages Just as you may have found it easier to use a computer operating system with a graphical user interface (GUI) , such as Windows 10 or macOS, programmers using visual programming languages may also take advantage of the GUI. For instance, programmers can easily add a command button to a screen with a few clicks of a mouse (see Figure TB7) instead of programming the button pixel by pixel and using many lines of code. Visual Basic.NET and Visual C# (pronounced as 'C-sharp') are two popular examples of visual programming languages.

## FIGURE TB5

A compiler translates the entire computer program into machine language, then the CPU executes the machine language program.

## FIGURE TB6

Interpreters read, translate, and execute one line of source code at a time.

## TABLE TB7 Examples of Popular Programming Languages

| Language       | Application             | Description                                                                                                                                                                                                                                                                                |
|----------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BASIC          | General purpose         | Beginner's All-Purpose Symbolic Interaction Code.An easy-to-learn language, BASIC works on almost all PCs.                                                                                                                                                                                 |
| C/C++          | General purpose         | C++ is a newer version of C. Developed atAT&T Bell Labs. Complex languages used for a wide range of applications.                                                                                                                                                                          |
| COBOL          | Business                | COmmon Business-Oriented Language. Developed in the 1960s, it was the first language for developing business software. COBOL is still frequently used for many business transaction processing applications on mainframes.                                                                 |
| FORTRAN        | Scientific              | FORmula TRANslator. The first commercial high-level language developed by IBM in the 1950s. Designed for scientific, mathematical, and engineering applications.                                                                                                                           |
| Java           | World Wide Web          | An object-oriented programming language developed by Sun Microsystems in the early 1990s. It is a popular programming language for the internet because it is highly transportable from one computer to another. Java is also used for programing Android apps as well as AI applications. |
| .NET Framework | World Wide Web          | A variety of programming languages (e.g., ASP.NET and C#) offered by Microsoft that can easily be integrated into web applications.                                                                                                                                                        |
| LISP           | Artificial Intelligence | LISt Processor. Dates from the late 1950s. One of the main languages used to develop applica- tions in artificial intelligence and high-speed arcade graphics.                                                                                                                             |
| PERL           | World Wide Web          | A dynamic programming language commonly used for writing scripts for websites, as well as for batch processing of large amounts of data.                                                                                                                                                   |
| Python         | General purpose         | Popular object-oriented scripting language; popular for AI projects                                                                                                                                                                                                                        |
| Objective-C    | App development         | Evolved from C, Objective-C is used for developing apps for iPhones, iPads, and Apple computers.                                                                                                                                                                                           |
| R              | Artificial Intelligence | Powerful language for advanced statistical analyses; frequently used for machine learning applications.                                                                                                                                                                                    |

## TABLE TB8 Concepts Related to Object-Oriented Languages

| Concept                        | Description                                                                                                                                                                       | Example                                                                                                                                                                          |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class                          | A set of objects having the same properties and behaviors (but the values of the properties can differ for each individual object). Classes can be reused for different programs. | A 'student' has an address and a grade-point average (GPA) (properties) and can enroll in courses (behavior).                                                                    |
| Object                         | Instantiation of a class.                                                                                                                                                         | Student Jeff Smith has a GPA of 3.94 and enrolls in MIS250.                                                                                                                      |
| Encapsulation                  | Data and behavior of a class are hidden from other classes and are thus protected from unexpected changes.                                                                        | The registrar does not need to know how the GPA is calculated within the 'student' class; the registrar cares only that it is updated.                                           |
| Inheritance                    | More specific classes include the properties and behaviors of the more general class.                                                                                             | Both 'distance degree student' and 'on-campus student' inherit properties (such as address and GPA) and behaviors (such as enroll in a course) from the general class 'student.' |
| Event-driven program execution | The programmer does not determine the sequence of execution for the program; the flow is determined by user input (e.g., mouse clicks) or messages from other applications.       | A word processor reacts to your typing and clicking.                                                                                                                             |

<!-- image -->

Web Development Languages You may have thought of creating a personal web page or already have one. In that event, you have some experience with using a markup language. The markup language you used to create your web page is called Hypertext Markup Language (HTML). HTML is a text-based file format that uses codes (i.e., tags) to specify the content and structure of a document; HTML tags are used to instruct the web browser on how a document should be presented to the user. Because many HTML editing programs are visually oriented and easy to use, you do not need to memorize the language to set up a web page. Programs for creating web pages (such as Brackets, Microsoft Visual Studio, and Adobe Dreamweaver CC) are called web page builders or HTML editors .

In HTML, the tags used to identify different elements on a page are set apart from the text with angle brackets (&lt;&gt;). Specific tags are used to mark the beginning and the ending of an element or a formatting command. For example, if you want text to appear in bold type, the HTML tag to begin bolding is &lt;b&gt;. The tag to turn off bolding, at the end of the selected text, is &lt;/b&gt;. The 'a href' command sets up a hyperlink from a word or image on the page to another HTML document. Tags can also be used to specify meaning, such as text to be used as the page title, levels of headings, the ends of paragraphs, emphasis, or importance, and to specify places to insert images or media (see Table TB9). The current HTML version is referred to as HTML5, which provides advanced markup for structuring and presenting content, such as the latest multimedia, on web pages. In addition to HTML, web developers use cascading style sheets (CSS) to specify

TABLE TB9 Common HTML Tags

| Tag                                       | Description                                                                                                    |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <html>...</html>                          | Delineates an HTML document                                                                                    |
| <head>...</head>                          | Contains the title, scripts, styles, metadata and other elements that are not displayed on the web page itself |
| <body>...</body>                          | Contains the visible portion of the document                                                                   |
| <b>...</b>                                | Creates bold text                                                                                              |
| <a href='https://www.arizona.edu'>...</a> | Creates a hyperlink                                                                                            |
| <a href='mailto:john@doe.com'>...</a>     | Creates a link creating a new email message                                                                    |
| <p>...</p>                                | Creates a new paragraph                                                                                        |
| <table>...</table>                        | Creates a table                                                                                                |

## FIGURE TB7

Visual Basic.Net, a visual programming language, is used to create standard business forms. Source: Visual Studio Community 2019, Windows 10, Microsoft Corporation.

## FIGURE TB8

A web page and the HTML source code used to create it. Source: Microsoft Edge, Windows 10, Microsoft Corporation.

the formatting and layout of elements on a web page (the current version, CSS3, provides greater flexibility for web page layouts, which allows for higher aesthetics and usability).

A good way to understand how HTML works is to find a web page you like, then use the 'View Source' command on your browser to view the markup used to create the page (see Figure TB8). Once you have created your own web page and saved it to a disk, you can upload it to a web space you have created through your website's host.

Markup languages such as HTML are for specifying the content and structure of web pages. If you want to add dynamic content or have users interact with your web page other than by clicking on hypertext links, then you will need to use special purpose programming languages such as Java or use web services, scripting languages, etc.

Java is  a  programming  language  that  was  developed  by  Sun  Microsystems  in  the  early 1990s to allow adding dynamic, interactive content to web pages. For example, the chat feature in the Blackboard learning environment uses Java. You can add Java applications to a web page in one of two ways: by learning Java or a similar language and programming the content you want or by downloading free general purpose applets from the web to provide the content you want on your web page. Applets are small programs that are executed within another application, such as a web page. When a user accesses your web page, the applets you inserted are downloaded from the server along with your web page to the user's browser, where they perform the desired action. Later, when the user leaves your web page, the web page and the applets disappear from his or her computer. Java is also frequently used to build Android apps.

Microsoft.NET is  a  programming  platform  that  is  used  to  develop  applications  that  are highly interoperable across a variety of platforms and devices. For example, using the .NET framework, developers can create an application that runs on desktop computers, mobile computers, or smartphones. A suite of visual programming languages including Visual C#, ASP.NET, and Visual Basic.NET can be used to construct .NET applications.

Scripting languages can also be used to supply interactive components and dynamic content to a web page. These languages let you build programs or scripts directly into HTML page code. Web page designers frequently use them to check the accuracy of user-entered information, such as names, addresses, and credit card numbers. Two common scripting languages are Microsoft's VBScript and JavaScript.

JavaScript bears little resemblance to Java. The two are similar, however, in that both Java and JavaScript are useful component software tools for creating dynamic, interactive web pages. That is, both allow users to add dynamic content to web pages. Both are also cross-platform programs, meaning that they can typically be executed by computers running Windows, Linux, Mac OS, and other operating systems.

Another common way to add dynamic content to websites is Flash. Flash animation is displayed on your screen using the Adobe Flash player. Yet Flash content is not well suited for mobile devices, and in 2010, Apple announced that it would not support Flash on its iPhones and iPads, rather advocating the use of HTML5, which allows for rich, interactive web applications.

<!-- image -->

Along with commercial products, there are several open source tools in wide use today. The most common is PHP, originally designed as a high-level tool for producing dynamic web content. The development of programming languages is an ongoing process of change and innovation, and these changes often result in more capable and complex systems for the user. The popularity of the internet has further spurred the creation of innovative and evolving software. From the pace of change that is occurring, many more innovations are on the horizon.

AI Development To approximate the functioning of the human brain and to enable capabilities such as computer vision, artificial intelligence makes heavy use of probabilities and statistics. As such, AI applications are typically developed using programming languages such as LISP, Prolog, or Python, but also in statistical languages such as R. Open source languages such as Python or R have become popular due to the wide availability of libraries (i.e., collections of subroutines) that programmers can draw on.

AUTOMATED DEVELOPMENT ENVIRONMENTS. Over the years, the tools for developing information systems have increased in both variety and capabilities. In the early days of systems development, a developer was left using pencil and paper to sketch out design ideas and program code. Computers were cumbersome to use and slow to program, and most designers worked out on paper as much of the system design as they could before moving to the computer. Today, system developers have a vast array of powerful computer-based tools at their disposal. These tools have forever changed the ways in which systems are developed. Computer-aided software engineering (CASE) refers to the use of automated software tools by systems developers to design and implement information systems. Developers can use CASE tools to automate or support activities throughout the systems development process with the objective of increasing productivity and improving the overall quality of systems. The capabilities of CASE tools are continually evolving and being integrated into a variety of development environments.

Types of CASE Tools Two of the primary activities in the development of large-scale information systems are the creation of design documents and the management of information. Over the life of a project, thousands of documents need to be created-from screen prototypes to database content and structure to layouts of sample forms and reports. At the heart of all CASE environments is a repository for managing such information.

CASE also helps developers represent business processes and information flows by using graphical diagramming tools. By providing standard symbols to represent business processes, information flows between processes, data storage, and the organizational entities that interact with the business processes, CASE eases a very tedious and error-prone activity (see Figure TB9). The tools not only ease the drawing process but also ensure that the drawings conform to development standards and are consistent with other design documents created by other developers.

<!-- image -->

## FIGURE TB9

System design diagram from Visio Professional for Microsoft 365.

Source: From Modern Systems Analysis and Design , 9th ed., published by Pearson Education, Inc.

## TABLE TB10 General Types of CASE Tools

| CASE Tool                    | Description                                                                                                                                                                           |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Diagramming tools            | Tools for graphically representing a system's processes, data, and control structures.                                                                                                |
| Screen and report generators | Tools that help model how systems look and feel to users. Screen and report genera- tors also make it easier for the systems analyst to identify data requirements and relationships. |
| Analysis tools               | Tools that automatically check for incomplete, inconsistent, or incorrect specifications in diagrams, screens, and reports.                                                           |
| Repositories                 | Tools that enable the integrated storage of specifications, diagrams, reports, and project management information.                                                                    |
| Documentation generators     | Tools that help produce both technical and user documentation in standard formats.                                                                                                    |
| Code generators              | Tools that enable the automatic generation of program and database definition code directly from the design documents, diagrams, screens, and reports.                                |

Source: Valacich and George (2020).

Another powerful capability of CASE is its ability to generate program source code automatically. CASE tools keep pace with contemporary programming languages and can automatically produce programming code directly from high-level designs in languages such as Java, Visual Basic.NET, and C#. In addition to diagramming tools and code generators, a broad range of other tools assists in the systems development process. The general types of CASE tools used throughout the development process are summarized in Table TB10.

## Foundational Topics in Networking

Telecommunications and networking technologies have become essential for supporting various business processes. Understanding how the underlying networking technologies work and where these technologies are heading will help you better understand the potential of information systems. The discussion begins with a description of the evolution of computer networking.

## Evolution of Computer Networking

Over the past decades, computer networking underwent an evolution from centralized computing to distributed computing to collaborative computing. These eras of computer networking are discussed next.

CENTRALIZED COMPUTING. Centralized computing , depicted in Figure TB10, remained largely unchanged through the 1970s. In this model, large centralized computers, called mainframes, were used to process and store data. During the mainframe era (beginning in the 1940s), people entered data on mainframes using local input devices called terminals . These devices were called 'dumb' terminals because they did not conduct any processing, or 'smart,' activities. The centralized computing model is not a true network because there is no sharing of data

<!-- image -->

## FIGURE TB10

In the centralized computing model, all processing occurs in one central mainframe.

and capabilities. The mainframe provides all the capabilities, and the terminals are only input/ output devices. Computer networks evolved in the 1980s when organizations needed separate, independent computers to communicate with each other. Centralized computing has seen a renaissance as businesses turn to thin clients to reduce costs for support, energy, or software licenses and to increase productivity and security.

DISTRIBUTED COMPUTING. The introduction of personal computers in the late 1970s and early 1980s gave individuals control over their own computing. Organizations also realized that they could use multiple small computers to achieve many of the same processing goals of a single large computer. Rather than using one mainframe to perform all the processing, people could work on independent subsets of tasks on separate computers and combine the individual results. To achieve this, computer networks were needed so that data and services could be easily shared between these distributed computers. The 1980s were characterized by an evolution to a computing model called distributed computing , in which separate computers work independently on subsets of tasks and then the individual results are pooled by communicating over a network. Distributed computing has seen a reemergence in the form of grid computing (see Chapter 3) and big data and analytics applications, where large data sets and/or computing tasks are broken into small chunks, each of which can be worked on by individual computers, and the individual results are combined to arrive at the end result, as depicted in Figure TB11.

COLLABORATIVE COMPUTING. In the 1990s, a new computing model, called collaborative computing , emerged. Collaborative computing is a synergistic form of distributed computing in which two or more networked computers work together to accomplish a common processing task. That is, in this model of computing, computers are not working independently on (more or less equivalent) subtasks, but have well-defined processing capabilities and responsibilities. For example, one computer may be used to store a large employee database. A second computer may be used to process and update individual employee records retrieved from this database. The two computers collaborate to keep the company's employee records current, as depicted in Figure TB12.

NETWORK SERVICES. Computer networks allow for sharing various capabilities between devices. For example, computer networks allow for efficiently storing, retrieving, and moving data between computers or allow for accessing network printers and network-attached storage devices; similarly, email, instant messaging, and the sending and receiving of pictures or video and audio data require the sender and recipient to be connected to a network. Finally, networks enable computers to share processing power, in that processing can be distributed between a client and a server. Clients request data or services from the servers. The servers store data and application programs. For example, the physical search of database records may take place on the server, while the user interacts with a much smaller database application that runs on the client.

<!-- image -->

## FIGURE TB11

In the distributed computing model, two or more networked computers work independently to accomplish subsets of a complex computing task.

## FIGURE TB12

In the collaborative computing model, two or more networked computers work together to accomplish a common task.

## FIGURE TB13

A LAN allows multiple computers located near each other to communicate directly with each other and to share peripheral devices, such as a printer.

<!-- image -->

When an organization decides to network its computers and devices, it must decide what services will be provided; typically, different services on the network are offered by different servers, such as print servers, email servers, etc. In addition to those servers, networks typically have specialized systems for managing the network, its users, and its resources. These include computers providing authentication services for  verifying  the  identity  of  users,  or directory services , which are repositories (or 'address books') containing information about users, user groups, resources on a network, access rights, etc.

## Types of Networks

Computing networks today include all three computing models: centralized, distributed, and collaborative. The emergence of new computing models did not mean that organizations completely discarded older technologies. Rather, a typical organizational computer network includes mainframes, servers, personal computers, and a variety of other devices. Computer networks are commonly classified by size, distance covered, and structure. The most common are described next.

PRIVATE BRANCH EXCHANGE. A private branch exchange (PBX) is a telephone system that serves a particular location, such as a business. It connects telephone extensions within the system and connects internal extensions to the outside telephone network. It can also connect computers within the system to other PBX systems, to an outside network, or to various office devices, such as fax machines or photocopiers. Since they use ordinary telephone lines, PBX systems have limited bandwidth, preventing them from transmitting such forms of data as video, digital music, or high-resolution photos. Using PBX technology, a business requires fewer outside phone lines, but must purchase or lease the PBX equipment. Many organizations now use Internet Protocol -based PBX systems, which make use of the organizations' data networks and allow for low-cost voice over IP calling.

LOCAL AREA NETWORK. A local area network (LAN), shown in Figure TB13, is a computer network that spans a relatively small area, allowing all computer users to connect with each other to share data and peripheral devices, such as printers. LAN-based communications may involve the sharing of data, software applications, or other resources between several users. LANs typically do not exceed tens of kilometers in size and are typically contained within a single building or a limited geographical area.

WIDE AREA NETWORK. A wide area network (WAN) is a computer network that spans a relatively large geographical area. WANs are typically used to connect two or more LANs. Different hardware

<!-- image -->

and transmission media are often used in WANs because they must cover large distances efficiently. Used by multinational companies, WANs transmit and receive data across cities and countries. A discussion follows of five specific types of WANs: campus area networks, metropolitan area networks, enterprise WANs, value-added networks, and global networks.

Campus Area Network A campus area network is a computer network that is used (and owned or leased) by a single organization to connect multiple LANs. A campus area network typically spans multiple buildings, such as at a corporate or university campus.

Metropolitan Area Network A metropolitan area network is a computer network of limited geographic scope, typically a citywide area, which combines LAN and high-speed fiberoptic technologies. Such networks are attractive to organizations that need high-speed data transmission within a limited geographic area.

Enterprise WAN An enterprise WAN is a WAN connecting disparate local area networks of a single organization into a single network (see Figure TB14).

Value-Added Network A value-added network is a private, third-party managed WAN typically used for B2B communications. With much B2B data communication taking place over the internet, providers focus on offering services such as secure email and translation of EDI standards to facilitate secure communication between businesses.

Global Network A global network spans multiple countries and may include the networks of several organizations. The internet is an example of a global network. The internet is the world's largest computer network, consisting of thousands of individual networks connecting billions of computers, smartphones, and other devices in almost every country of the world.

PERSONAL AREA NETWORK. A final type of computer network, called a personal area network, uses wireless communication to exchange data between computing devices using short-range radio communication, typically within an area of 10 meters (30 feet). The enabling technology for personal area networks is Bluetooth , a specification for personal networking of desktop computers, peripheral devices, mobile phones, portable media players, and various other devices. Bluetooth is integrated into a variety of personal devices to ease interoperability and information sharing (see Figure TB15).

Now that you understand the general types of networks, the next sections examine some further fundamental concepts. After discussing packet switching as a concept for sharing communication channels, we will delve deeper into network standards and technologies. Together, these sections provide a foundation for understanding various types of networks.

<!-- image -->

## FIGURE TB14

An enterprise network allows an organization to connect distributed locations into a single network.

## FIGURE TB15

Bluetooth is used to exchange data between devices using shortrange radio communication. Source: Nor Gal/Shutterstock.

## FIGURE TB16

Computers A and B use packet switching to send messages or files to computers C and D.

<!-- image -->

## Packet Switching

Telecommunications advances have enabled connecting individual computer networksconstructed with a variety of hardware and software-together in what appears to be a single network. To enable rapid transmission of massive amounts of data, most data networks rely on packet switching. Packet switching is based on the concept of turn taking and enables millions of users to send large and small chunks of data across the network concurrently. To minimize delays, network technologies limit the amount of data that any computer can transfer on each turn. Consider a conveyor belt as a comparison. Suppose that the conveyor belt connects a warehouse and a retail store. When a customer places an order, it is sent from the store to the warehouse, where a clerk assembles the items in the order. The items are placed on the conveyor belt and delivered to the customer in the store. In most situations, clerks finish sending items from one order before proceeding to send items from another order. This process works well when orders are small, but when a large order with many items comes in, sharing a conveyor belt can introduce delays for others. Consider waiting in the store for your one item while another order with 50 items is being filled.

Most networks, including local area networks (LANs), WANs, and the internet use packetswitching technologies to minimize delivery delays when users share the communication channel. Figure TB16 illustrates how computers use packet switching. Computer A wants to send a message to computer C; similarly, computer B wants to send a message to computer D. For example, computer A is trying to send an email message to computer C, while computer B is trying to send a word processing file to computer D. The outgoing messages are divided into smaller packets of data, and then each sending computer (A and B) takes turns sending the packets over the transmission medium. The incoming packets are reassembled at their respective destinations, using previously assigned packet sequence numbers.

For packet switching to work, each computer attached to a network must have a unique network address, and each packet being sent across a network must be labeled with a header containing

<!-- image -->

the network address of the source (sending computer) and the network address of the destination (receiving computer). As packets are transmitted, network hardware detects whether a particular packet is destined for a local machine. Packet-switching systems adapt instantly to changes in network traffic. If only one computer needs to use the network, it can send data continuously. As soon as another computer needs to send data, packet switching, or turn taking, begins. Next, we explain the importance of network standards and protocols to enable data communication.

## Network Standards and Protocols

Standards play a key role in creating networks. The physical elements of networks-adapters, cables, and connectors-are defined by a set of standards that have evolved since the early 1970s. Standards ensure the interoperability and compatibility of network devices, and each standard combines a media access control technique, network topology, and transmission media in different ways. The dominant standard for wired local area networks is 802.3, typically referred to as Ethernet; wireless local area networks are based on the 802.11 family of standards. These standards are continuously evolving, and other competing standards for local area networks have all but vanished. Software interacts with hardware to implement protocols that allow different types of computers and networks to communicate successfully.

PROTOCOLS. All networks employ protocols to make sure communication between computers is successful. Protocols are agreed-on formats for transmitting data between connected computers. They specify how computers should be connected to the network, how transmission errors will be detected, what data compression method will be used, how a sending computer will signal that it has finished sending a message, and how a receiving computer will signal that it has received a message. Protocols allow packets to be correctly routed to and from their destinations. There are literally thousands of protocols to choose from, but a few are a lot more important than the others. In this section, we will first review the OSI model, the worldwide standard for implementing protocols. Then, we briefly review TCP/IP, the protocol used by the internet, and Ethernet, a commonly used protocol for local area networks.

The OSI Model The need of organizations to interconnect computers and networks that use different protocols has driven the industry to an open systems architecture in which different protocols can communicate with each other. The International Organization for Standardization defined a networking model called Open Systems Interconnection (OSI), which divides computer-to-computer communications into seven connected layers. The Open Systems Interconnection (OSI) model represents a group of specific tasks (represented in Figure TB17) as successive layers that enable computers to communicate data. Each successively higher layer builds on the functions of the layers below. For example, suppose you are using a PC running Windows and are connected to the internet, and you want to send a message to a friend who uses a large workstation computer running Unix-two different computers and two different operating systems. When you transmit your message, it is passed down from layer to layer in the Windows protocol environment of your system. At each layer, special bookkeeping information specific to the layer, called a header, is added to the data. Eventually, the data and headers are transferred from the Windows layer 1 to Unix's layer 1 over some physical pathway. On receipt, the message is passed up through the layers in the Unix application. At each layer, the

<!-- image -->

## FIGURE TB17

The OSI model has seven layers and provides a framework for connecting different computers with different operating systems to a network.

## FIGURE TB18

Message passing between two different computers.

<!-- image -->

corresponding header information is stripped away, the requested task is performed, and the remaining data package is passed on until your message arrives as you sent it, as shown in Figure TB18. In other words, protocols represent an agreement between different parts of the network about how data are to be transferred.

Transmission Control Protocol/Internet Protocol (TCP/IP) Because so many different networks are interconnected throughout the world, they must have a common language, or protocol, to communicate. The protocol used by the internet is called Transmission Control Protocol/ Internet Protocol (TCP/IP). Whereas TCP is responsible for breaking down a message into smaller packets, creating a connection between two computers, and ensuring that data are reliably transmitted and arrive in the correct sequence, IP is responsible for addressing and correct routing of packages from source to destination. First, TCP breaks data into small chunks and manages the transfer of those packets from computer to computer via packet switching. For example, a single document may be broken into several packets, each containing several hundred characters, as well as a destination address (the IP part of the protocol). The IP part defines how a data packet must be formed and to where a router (an intelligent device used to connect two or more individual networks) must forward each packet. A data packet that conforms to the IP specification is called an IP datagram . Datagram routing and delivery are possible because, as previously mentioned, every computer and router connected to the internet is assigned a unique address, called its IP address. When an organization connects to the internet, it obtains a set of IP addresses that it can assign to its computers. Packets travel independently to their destination, sometimes following different paths and arriving out of sequence. The destination computer reassembles all the packets on the basis of their identification and sequencing information: TCP helps IP guarantee delivery of datagrams by performing three main tasks. First, it automatically checks for datagrams that may have been lost en route from their source to their destination. Second, TCP collects the incoming datagrams and puts them in the correct sequence to re-create the original message. Finally, TCP discards any duplicate copies of datagrams that may have been created by network hardware. Together, TCP and IP provide a reliable and efficient way to send data across the internet.

Ethernet Ethernet is a set of LAN protocols using packet switching developed by the Xerox Corporation in 1976. Different types of data (including IP datagrams) can travel on Ethernets by being enclosed in another set of headers to form packets called Ethernet frames. The original Ethernet

protocol supports data transfer rates of 10 Mbps. A later version, called 100Base-T or Fast Ethernet, supports transfer rates of 100 Mbps; the latest version, called 100 Gigabit Ethernet (100GbE), supports transfer rates of 100 Gbps, or 100,000 Mbps, over relatively large distances. Most new computers have a network interface card (also known as network adapter or Ethernet card) installed, allowing you to use the Ethernet protocol to connect to broadband modems, home networks, or work networks. Each network adapter has a unique identifier (called MAC address, assigned by the manufacturer) that is used to identify the computer on the network. The PC is then connected to other network components via transmission media, such as Ethernet cables. Increasingly, organizations use the Ethernet protocol for wide area networks, called Wide Area Ethernet or Ethernet W AN.

NETWORK TOPOLOGIES. Network topology refers to the shape of a network. The four basic network topologies are star, ring, bus, and mesh. A star network is configured, as you might expect, in the shape of a star, as shown in Figure TB19a. That is, all nodes or workstations are connected to a central hub through which all messages pass. The workstations represent the points of the

## FIGURE TB19

(a) The star network has several workstations connected to a central hub. (b) The ring network is configured in a closed loop, with each workstation connected to another workstation. (c) The bus network is configured in the shape of an open-ended line where each workstation receives the same message simultaneously. (d) The mesh network consists of computers and other devices that are either fully or partially connected to each other.

<!-- image -->

star. Star topologies are easy to lay out and modify. However, they are also the costliest because they require the largest amount of cabling. Although it is easy to diagnose problems at individual workstations, star networks are susceptible to a single point of failure at the hub that would result in all workstations losing network access. This topology is used in switched Ethernet local area networks, where all devices are connected to a central switch. A ring network is configured in the shape of a closed loop or circle with each node connecting to the next node, as shown in Figure TB19b. In ring networks, messages move in one direction around the circle. As a message moves around the circle, each workstation examines it to see whether the message is for that workstation. If not, the message is regenerated and passed on to the next node. This regeneration process enables ring networks to cover much larger distances than star or bus networks can. Relatively little cabling is required, but a failure of any node on the ring network can cause complete network failure. Selfhealing ring networks avoid this by having two rings with data flowing in different directions; thus, the failure of a single node does not cause the network to fail. In either case, it is difficult to modify and reconfigure a ring network. Although sometimes used in WANs, ring topologies are not commonly used in LANs anymore. A bus network is in the shape of an open-ended line, as shown in Figure TB19c; as a result, it is the easiest network to extend and has the simplest wiring layout. This topology enables all network nodes to receive the same message through the network cable at the same time. However, it is difficult to diagnose and isolate network faults. Whereas early variants of Ethernet used bus networks, they are not commonly used any more. Finally, a mesh network consists of computers and other devices that are either fully or partially connected to each other. In a full mesh design, each computer and device is connected to every other computer and device. In a partial mesh design, many but not all computers and devices are connected (see Figure TB19d). Like a ring network, mesh networks provide relatively short routes from one node to another. Mesh networks also provide many possible routes through the network-a design that prevents one circuit or computer from becoming overloaded when traffic is heavy. Given these benefits, most WANs, including the internet, use a partial mesh design.

MEDIA ACCESS CONTROL. Media access control is the set of rules that governs how a given node or workstation gains access to the network to send or receive data. Without media access control, collisions are likely to happen if two or more workstations simultaneously transmit messages on the network. There are two general types of media access control: distributed and random access. With distributed access control, only a single workstation at a time has authorization to transmit its data. One method of authorization is token passing, where authorization is transferred sequentially from workstation to workstation. Ring networks normally use a token-passing media access control method to regulate network traffic. Another method, polling, uses a master device that centrally controls access to the network by sequentially polling each connected device whether it needs to transmit data. Under random access control (sometimes referred to as contention-based), any workstation can transmit data by checking whether the medium is available. No specific permission is required. A commonly used method of random-access control in wireless LANs is called carrier sense multiple access/collision avoidance (CSMA/CA) . In CSMA/CA, each connected device 'listens' to traffic on the transmission medium to determine whether a message is being transmitted. If no traffic is detected, the device sends its message; otherwise, it waits. Modern Ethernet local area networks use switches to do away with the problem of collisions altogether: Each device is connected to a switch, which connects the different devices as needed for transmitting data; in other words, the switch creates separate point-to-point circuits between devices, such that a message is not broadcast to all devices but only travels between the sender and the receiver.

## Network Technologies

Typically, devices in a network are not connected directly to each other; rather, computer networks rely on different networking hardware components to connect computers and route messages. In addition, individual devices and hardware components are connected using different wired or wireless media. These are discussed next.

NETWORKING HARDWARE. Because of the complexity of current networks, a variety of specialized pieces of equipment have been developed for computers to connect and transfer data. However, not all pieces of equipment are necessary for connecting computers together, and the use of this equipment is dependent on the intended use and configuration of the network. Table TB10 presents some commonly used types of networking equipment to meet businesses' networking needs. Some of these devices are also commonly used in home networks; for

## TABLE TB10 Networking Hardware

| Networking Hardware   | Description                                                                                                                                                                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Switch                | A switch is used to connect multiple computers, servers, or printers to create a network. Switches typically inspect data packets received and forward them to the correct addressee.                                                                                                                                                    |
| Router                | A router is an intelligent device used to connect two or more different networks. When a router receives a data packet, it looks at the network address and passes the packet on to the appropriate network. Routers are commonly used to connect a LAN to a WAN, such as the internet, or a wired to a wireless network.                |
| Wireless access point | A wireless access point transmits and receives wireless (Wi-Fi) signals to allow wireless devices to connect to the network.                                                                                                                                                                                                             |
| Wireless controller   | A wireless controller manages multiple access points and can be used to manage transmission power and channel allocation to establish desired coverage throughout a building and minimize interference between individual access points. Further, wireless controllers can be used to manage authentication and other security features. |

example, your DSL modem may also act as a router and wireless access point. Other networking devices used by telecommunications companies are beyond the scope of this discussion.

CABLE MEDIA. Cable media physically link computers and other devices in a network. The most common forms of cable media are twisted pair, coaxial, and fiber-optic.

Twisted-Pair Cable Twisted-pair (TP) cable is made of two or more pairs of insulated copper wires twisted together (see Figure TB20). TP cables are rated according to quality (in terms of the ability to transmit high frequency signals and the 'crosstalk' between individual wires); category 3 (Cat 3), Cat 5, Cat 6, Cat 7, and Cat 8 cables are often used in network installations. Depending on the rating, TP cables have a capacity of up to 40 gigabits per second (Gbps) at distances of up to 100 meters (330 feet); faster speeds can be achieved over shorter distances. The cable may be unshielded (UTP, such as Cat 3, Cat 5, or Cat 6) or shielded (STP, such as Cat 7 or Cat 8). Telephone wire installations as well as many local area networks use UTP cabling, as it is cheap and easy to install. However, like all copper wiring, it has rapid attenuation and is very sensitive to electromagnetic interference (EMI) and eavesdropping-the undetected capturing of data transmitted over a network. STP uses wires wrapped in insulation, making it less prone to EMI and eavesdropping. Ethernet cables typically use RJ-45 connectors so that they can be plugged into a network adapter or into other network components.

## FIGURE TB20

(a) A cable spliced open showing several twisted pairs. (b) A sample network installation that utilizes many TP cables at once. Sources: (a) Georgios alexandris/Shutterstock; (b) Inara Prusakova/Shutterstock.

<!-- image -->

(b)

<!-- image -->

## FIGURE TB21

These coaxial cables are ready to be connected to a computer or other device.

Source: Kasia/Shutterstock.

## FIGURE TB22

Fiber-optic cable consists of a light-conducting glass or plastic core, surrounded by more glass, called cladding, and a tough outer sheath. Source: Sashkin/Shutterstock.

<!-- image -->

Coaxial Cable Coaxial (or coax) cable contains a solid inner copper conductor surrounded by plastic insulation and an outer braided copper or foil shield (see Figure TB21). Coax cable comes in a variety of thicknesses-thinnet coax and thicknet coax-based on resistance to EMI. Although less costly than TP, thinnet coax is not commonly used in networks anymore; thicknet coax is more expensive than TP. Coax cable is most commonly used for cable television installations and for networks operating at 10 to 100 megabits per second (Mbps). Its attenuation is lower than that of TP cable, and it is moderately susceptible to EMI and eavesdropping.

Fiber-Optic Cable Fiber-optic cable is made of a light-conducting glass or plastic core surrounded by more glass, called cladding, and a tough outer sheath (see Figure TB22). The sheath protects the fiber from changes in temperature as well as from bending or breaking. This technology uses pulses of light sent along the optical cable to transmit data. Fiber-optic cable transmits clear and secure data because it is immune to EMI and eavesdropping. Transmission signals do not break up because fiber-optic cable has low attenuation. It is also extremely fast. Practically, it can achieve over 1 Gbps at distances up to 25 kilometers (15 miles). In the lab, researchers have exceeded 43 terabits per second-that is, the entire contents of a 1TB

<!-- image -->

hard drive in a fifth of a second. Each year, in a manner like increasing CPU performance and Moore's law, researchers are discovering new ways to rapidly increase the capacity of fiber optic cables. Fiber-optic cable is more expensive than copper wire because the cost and difficulties of installation and repair are higher for fiber-optic. Fiber-optic cables are used for high-speed backbones -the high-speed central networks to which many smaller networks can be connected. A backbone may connect, for example, several different buildings in which other, smaller LANs reside. Submarine telecommunications cables (used for telephone and internet traffic between continents) also use fiber-optic cable. In home environments, fiber-optic cable can be used to connect digital audio devices.

WIRELESS MEDIA. With the popularity of mobile devices such as laptops, tablets, and smartphones, wireless media are rapidly gaining popularity. Wireless media transmit and receive electromagnetic signals using methods such as infrared line of sight, high-frequency radio, and microwave systems.

Infrared Line of Sight Infrared line of sight uses high-frequency light waves to transmit signals on an unobstructed path between nodes. While commonly being used in remote controls for most audiovisual equipment, such as TVs, stereos, and other consumer electronics equipment, infrared systems are not well suited for rapidly transmitting large amounts of data; thus, this technology has since been surpassed by Wi-Fi and Bluetooth for data communication.

High-Frequency Radio High-frequency radio signals can transmit data at rates of up to several hundred Mbps to network nodes from 12.2 up to approximately 40 kilometers (7.5 to 25 miles) apart, depending on the nature of any obstructions between them. The flexibility of the signal path makes high-frequency radio ideal for mobile transmissions. For example, most police departments use high-frequency radio signals that enable police vehicles to communicate with each other as well as with the dispatch office. This medium is expensive because of the cost of antenna towers and high-output transceivers. Installation is complex and often dangerous because of the high voltages. Although attenuation is fairly low, this medium is very susceptible to EMI and eavesdropping.

Two common applications of  high-frequency  radio  communication  are  cellular  phones  and wireless networks. A cellular phone gets its name from how the signal is distributed. In a cellular system, a coverage area is divided into cells with a low-powered radio antenna/receiver in each cell; these cells are monitored and controlled by a central computer (see Figure TB23). Any given cellular network has a fixed number of radio frequencies. When a user initiates or receives a call, the mobile telephone switching office assigns the caller a unique frequency for the duration of the call. As a person travels within the network, the central computer at the switching office monitors the quality of the signal and automatically assigns the call to the closest cellular antenna. Cellular phones have gone through rapid changes since their first commercial use in the mid-1980s (see Table TB11). Because of the costs involved in setting up fixed telephone lines, cellular phones have become very popular in many developing countries and are a key factor in bridging the digital divide.

<!-- image -->

## FIGURE TB23

A cellular network divides a geographic region into cells.

## TABLE TB11 Evolution of Cell Phone Technology

| Generation   | Description                                                                                                                                                       | Data Transfer                                                        | Advantages                                                                                                                       |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 0G           | Preceded modern cellular mobile telephony and was usually mounted in cars or trucks; it was a closed circuit, so you could call only other radio telephone users. | Analog                                                               | Enabled communicating on the go.                                                                                                 |
| 1G           | This technology, introduced in the 1980s, used circuit switching; it had poor voice quality, unreliable handoffs between towers, and nonexistent security.        | Analog                                                               | Enabled users to communicate with other cell phones and land lines.                                                              |
| 2G           | The first all-digital signal that was divided intoTDMA and CDMA standards. Allowed for SMS (text) messaging and emails to be sent/received.                       | Digital (up to 9.6 Kbps transfer)                                    | Lower-powered radio signals allowed for longer battery life. Digital format allowed for clearer signal and reduced signal noise. |
| 2.5G         | Allows for faster data transmission via a packet-switched domain in addition to the circuit-switched domain.                                                      | Digital (up to 115 Kbps transfer)                                    | Higher data speeds allowed for more complex data to be transmit- ted (e.g., sports scores and news stories).                     |
| 3G           | Even faster. Requires a new cellular net- work, different from that already available in 2G systems.                                                              | Digital (minimum of 384 Kbps when moving and 2 Mbps when stationary) | Transfer full video and audio.                                                                                                   |
| 4G           | Set of standards for high-speed mobile con- nectivity. Different standards on different networks and locations.                                                   | Digital (up to 100 Mbps when moving and 1 Gbps when stationary)      | Data speeds similar to wired networks.                                                                                           |
| 5G           | Evolving set of standards for ultra-high speed, low latency stationary and mobile connectivity.                                                                   | Digital (peak data rates of up to 20 Gbps)                           | Extremely high speed and low latency, enabling various IoT applications.                                                         |

One of the most significant advances in cellular technology was the introduction of packet switching for data transmission as operators moved from 2G to 2.5G. While 3G networks have seen widespread deployment, data rates were still limited. The introduction of 4G cellular networks provided mobile broadband internet access, supporting mobile web access, IP telephony (e.g., Skype), game services, high-definition mobile TV , and videoconferencing. There are competing standards for deploying 4G services; two notable standards are HSPA+ and LTE (long-term evolution). Each standard supports different data rates and distances. Nevertheless, they all are significantly faster than existing 3G networks. HSPA+ (High Speed Packet Access) is a family of high-speed 3G and 4G digital data services available to mobile carriers worldwide that helps to extend the capabilities of existing infrastructures; as an upgrade of 3G technologies, some do not consider it 'true' 4G. LTE uses an all IP-based architecture where everything (including voice) is handled as data, similar to the internet. Each standard continues to evolve and gain (or lose) market share and acceptance with different global carriers; given advantages in terms of speed, LTE is currently the predominant 4G standard in the United States. 5G promises to be up to ten times as fast as 4G, provide better coverage, and more efficiently utilize the increasingly limited wireless spectrum. 5G promises extremely low latency (i.e., the time it takes for a data packet to travel from its origin to the destination and back), which is crucial for applications requiring near-real time connectivity, such as drones, self-driving cars, healthcare monitoring systems, or various other IoT applications. Yet, whereas 5G promises many benefits, clear downsides are smaller cell sizes (meaning that more cell towers are required), high installation costs, and unresolved privacy and security issues. Further, 5G standards are still evolving, and governments are critically evaluating the risks of relying on certain companies to provide key parts of the communications infrastructure of the future.

High-frequency radio-wave technology is increasingly being used to support wireless local area networks (WLANs). WLANs based on a family of standards called 802.11 are also referred to as Wi-Fi (wireless fidelity). The 802.11 family of standards has been universally adopted and

<!-- image -->

<!-- image -->

has transmission speeds up to 450 Mbps (using the 802.11n standard), with even faster standards currently under development. The ease of installation has made WLANs popular for business and home use. For example, many homes and buildings have multiple computers or mobile devices and need (or want) to share internet access, files, and peripheral devices. Unfortunately, many older buildings and homes do not have a wired infrastructure to easily connect computers and devices, making wireless networking particularly attractive. Using wireless technologies, many organizations  are  transforming  their  work  environments  into  better  team  collaboration environments.

Microwave Transmission Microwave transmission uses high-frequency radio signals that are sent through the air using either terrestrial (earth-based) systems or satellite systems (microwaves are typically of shorter wavelength and thus higher frequency than radio waves used by cellular or Wi-Fi networks). Terrestrial microwave, shown in Figure TB24, uses antennae that require an unobstructed path or line of sight between nodes. The cost of a terrestrial microwave system depends on the distance to be covered. Typically, businesses lease access to these microwave systems from service providers rather than invest in antenna equipment. Data may be transmitted at up to 274 Mbps. Over short distances, attenuation is not a problem, but signals can be disrupted over longer distances by environmental conditions such as high winds and heavy rain. EMI and eavesdropping are significant problems with microwave communications.

Satellite microwave, shown in Figure TB25, uses satellites orbiting the earth as relay stations to transfer signals between ground stations located on earth. Satellites orbit from 400 to 22,300 miles above the earth and have different uses and characteristics (see Table TB12). Because of the distance signals must travel, satellite transmissions are delayed (also known as propagation delay ). Satellite transmission has become very viable for media such as TV and radio; e.g., the digital radio station SiriusXM has its own satellites that send out scrambled signals to proprietary receivers.

<!-- image -->

## FIGURE TB24

Terrestrial microwave requires a line-of-sight path between a sender and a receiver.

## FIGURE TB25

Communications satellites are relay stations that receive signals from one earth station and rebroadcast them to another.

## TABLE TB12 Characteristics of Satellites with Different Orbits

| Name                             | Distance from Earth   | Characteristics/Common Application                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Low Earth Orbit (LEO) Satellite  | 400-1,000 miles       | ■ Not fixed in space in relation to the rotation of the earth; circles the earth several times per day. ■ Photography for mapping and locating mineral deposits; monitoring ice caps, coast- lines, volcanoes, and rain forests; researching plant and crop changes; monitoring wildlife habitats and changes; search and rescue for downed aircraft or ships that are in trouble; research projects in astronomy and physics. |
| Medium Earth Orbit (MEO)         | 1,000-22,300 miles    | ■ Not fixed in space in relation to the rotation of the earth; circles the earth more than one time per day. ■ Primarily used in geographical positioning systems (such as GPS) for navigation of ships at sea, spacecraft, airplanes, automobiles, and military weapons.                                                                                                                                                      |
| Geosynchronous Earth Orbit (GEO) | 22,300 miles          | ■ Fixed in space in relation to the rotation of the earth; circles the earth one time per day. ■ Because it is fixed in relation to the earth, transmission is simplified. ■ Transmission of high-speed data for television, weather information, remote internet connections, digital satellite radio, and telecommunications (satellite phones).                                                                             |

Another strength of satellite communication is that it can be used to access very remote and undeveloped locations on the earth. Yet such systems are extremely costly because their use and installation depends on space technology. Companies such as AT&amp;T sell satellite services with typical transmission rates ranging from less than 1 to 10 Mbps, but the rates can be as high as 90 Mbps. Like terrestrial microwave, satellite systems are prone to attenuation and are susceptible to EMI and eavesdropping. Table TB13 compares wireless media across several criteria.

## The Internet

The name internet is derived from the concept of internetworking , which means connecting host computers and their networks to form even larger networks. The internet is a large worldwide collection of networks that uses a common protocol to communicate. In the following sections, we discuss in more detail how independent networks are connected to form the internet, who manages the internet, and how home and business users can connect to the internet.

HOW DID THE INTERNET GET STARTED? You can trace the roots of the internet back to the late 1960s, when the U.S. Defense Advanced Research Projects Agency (DARPA) began to study ways to interconnect networks of various kinds. This research effort produced the Advanced Research Projects Agency Network (ARPANET) , a large wide area network (WAN) that linked many universities and research centers. The first two nodes on the ARPANET were the University of California, Los Angeles, and the Stanford Research Institute, followed by the University of California, Santa Barbara, and the University of Utah.

ARPANET quickly evolved and was combined with other networks. For example, in 1986, the U.S. National Science Foundation (NSF) initiated the development of the National Science Foundation Network (NSFNET) , which became a major component of the internet. Other networks  throughout  the  United  States  and  the  rest  of  the  world  were  interconnected  and/or morphed into the growing 'internet.' Throughout the world, support for the internet has come

## TABLE TB13 Relative Comparison of Wireless Media

| Medium                 | Expense   | Speed          | Attenuation   | EMI   | Eavesdropping   |
|------------------------|-----------|----------------|---------------|-------|-----------------|
| Infrared line of sight | Low       | Up to 16 Mbps  | High          | High  | High            |
| High-frequency radio   | Moderate  | Up to 300 Mbps | Low           | High  | High            |
| Terrestrial microwave  | Moderate  | Up to 274 Mbps | Low           | High  | High            |
| Satellite microwave    | High      | Up to 90 Mbps  | Moderate      | High  | High            |

<!-- image -->

from a combination of federal and state governments, universities, national and international research organizations, and industry.

CONNECTING INDEPENDENT NETWORKS. The internet uses routers to interconnect independent networks. For example, Figure TB26 illustrates a router that connects Networks 1, 2, and 3. A router, like a conventional computer, has a central processor, memory, and network interfaces. However, routers do not use conventional software, nor are they used to run applications. Their only job is to interconnect networks and forward data packets from one network to another. As illustrated in Figure TB26, Computers A and F are connected to independent networks. If Computer A generates a data packet destined for Computer F, the packet is sent to the router that interconnects the two networks. The router forwards the packet on to Network 2, where it is delivered to its destination at Computer F.

Routers are the fundamental building blocks of the internet because they connect thousands of LANs and WANs. LANs are connected to backbone WANs, as depicted in Figure TB27. A backbone network manages the bulk of network traffic and typically uses a higher-speed connection than the individual LAN segments. For example, a backbone network might use fiber-optic cabling, which can transfer data at a rate of 100 Gbps, whereas a LAN connected to the backbone may use Ethernet with TP cabling, transferring data at a rate of 10 Mbps to 10 Gbps. To gain access to the internet, an organization installs a router between one of its own networks and the network of its internet service provider. Business organizations typically connect to the internet not only with personal computers but with web servers as well.

<!-- image -->

## FIGURE TB26

Routers connect independent networks.

## FIGURE TB27

LANs connect to wide area backbones.

WHO MANAGES THE INTERNET? Individual computers on the internet are identified by their IP addresses. So, who keeps track of these IP addresses on the internet? A number of national and international standing committees and task forces have been formed to manage the development and use of the internet. Most notably, the Internet Assigned Numbers Authority is responsible for managing global and country code top-level domains as well as global IP number space assignments. In addition, the Internet Assigned Numbers Authority provides central maintenance of the Domain Name System (DNS) root database, which points to distributed DNS servers replicated throughout the internet. This database is used to associate internet host names with their IP addresses. Users can access websites using domain names or IP addresses. The functionality of the DNS is to provide users easy-to-remember domain names to access websites. In other words, it is far easier to remember www.apple.com than it is to remember 17.178.96.59 (the IP address of a server mirroring Apple's content as of mid-2020), but both will work as addresses in any web browser, as the DNS servers will translate the domain names into the accompanying IP address.

In 1993, the NSF created InterNIC , a government-industry collaboration, to manage directory and database services, domain registration services, and other information services on the internet. In the late 1990s, this internet oversight was transitioned more fully out into industry when InterNIC morphed into the Internet Corporation for Assigned Names and Numbers , a nonprofit corporation that assumed responsibility for managing IP addresses, domain names, and root server system management. Using 32-bit addresses, IPv4 provided 2 32 IP addresses (about 4.29 billion addresses). With the increase of devices connected to the internet, the number of unassigned internet addresses is running out, so new classes of addresses were being added as IPv6 , the latest version of the IP, was adopted in June 2012. Using 128-bit addresses, IPv6 provides 2 128 addresses, allowing literally trillions and trillions of devices to be connected to the internet.

HOW TO CONNECT TO THE INTERNET. Now you can see how the internet works and how it is managed. How do you connect to the internet? For personal use (i.e., from home), we typically connect to the internet through an internet service provider (ISP) , also called an internet access provider . ISPs provide several different ways to access the internet from home (see Table TB14).

## TABLE TB14 Methods for Connecting to the Internet

| Service                             | Current Status and Future Outlook                                                                                                                                                                                                                                      | Typical Bandwidth                             |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Dial-up                             | Although still used in the United States, there are very few new dial-up customers. This market should dry up as broadband moves to rural areas and developing nations.                                                                                                | 52 Kbps                                       |
| Integrated Services Digital Network | This technology has limited market share because of its expense. Typically, these connections are more expensive than broadband connections, although they offer less bandwidth.                                                                                       | 128 Kbps                                      |
| Cable                               | Coaxial cable used for cable TV provides much greater bandwidth than tele- phone lines and therefore is the market leader in broadband use for home users. Overselling of bandwidth that causes slower-than-average speeds tends to be a major problem for home users. | Upload: up to 31 Mbps Download: up to 43 Mbps |
| DSL                                 | DSL technology has gained market share from cable. With many companies offering higher speeds at lower cost, DSL should continue to cut into cable's market share.                                                                                                     | Upload: up to 16 Mbps Download: 1.5-50 Mbps   |
| Satellite                           | Although satellite connectivity had a promising future, many users are mov- ing away from this expensive technology in favor of faster and cheaper cable or DSL connections.                                                                                           | Upload: 50 Kbps Download: 5 Mbps              |
| Wireless broadband                  | Wireless broadband offers the most promise of any of the current technolo- gies, as the speeds are increasing while the coverage areas continue to grow.                                                                                                               | Up to 1 Gbps                                  |
| Fiber to the home                   | Fiber to the home has been adopted by several major players in the ISP industry. The demand for fast connections is helping make this a significant technology for ISPs.                                                                                               | At least 100 Mbps, up to 1000 Mbps            |

<!-- image -->

ISPs connect to one another through internet exchange points . Much like railway stations, these serve as access points for ISPs and are exchange points for internet traffic. They determine how traffic  is  routed  and  are  often  the  points  of  most  internet  congestion.  Internet  exchange points are a key component of the internet backbone , which is the collection of main network connections and telecommunications lines that make up the internet (see Figure TB28).

The internet follows a hierarchical structure, similar to the interstate highway system. Highspeed backbone network lines are like interstate highways, enabling traffic from midlevel networks to get on and off. Think of midlevel networks as city streets that, in turn, accept traffic from their neighborhood streets or member networks. However, you cannot get on an interstate or city street whenever you want to. You must share the highway and follow traffic control signs to arrive safely at your destination. The same holds true for traffic on the internet, and people can connect to the internet in a number of ways. In the next section, we outline how typical home users connect to the internet.

Dial-Up Years ago, most people connected to the internet through a telephone line at home or work. The term we use for connecting via a standard telephone lines is plain old telephone service (POTS) (the POTS system is also called the public switched telephone network [PSTN] ). POTS was designed to pass sounds in the form of analog signals -signals consisting of a continuous wave that can take on an infinite number of values within its frequency range. However, computers use electrical pulsesdigital signals -that consist of discrete 'on' and 'off' values. The only way to pass digital data over conventional voice telephone lines is to convert it to audio tones-analog signals-that the telephone lines can carry. A modem (MOdulator/ DEModulator) converts digital signals from a computer into analog signals so that telephone lines may be used as a transmission medium to send and receive digital signals, as shown in Figure TB29. As the speed, or bandwidth, of POTS is generally only about 52 Kbps (52,000 bits per second), today most people connect to the internet using some form of digital, high-speed connection.

Integrated Services Digital Network Integrated services digital network (ISDN) is a standard for worldwide digital communications. ISDN was designed in the 1980s to replace all analog systems, such as most telephone connections in the United States, with a completely digital transmission system. ISDN uses existing TP telephone wires to provide high-speed data service. ISDN systems can transmit voice, video, and data. Because ISDN is a purely digital network, you can connect your PC to the internet without the use of a traditional modem.

## FIGURE TB28

The internet backbone.

## FIGURE TB29

Modems convert digital signals into analog and analog signals into digital.

<!-- image -->

Removing the analog-to-digital conversion for sending data and the digital-to-analog conversion for receiving data and higher bandwidth greatly increases the data transfer rate. However, a small electronic box called an ISDN modem is typically required so that computers and older, analog-based devices such as telephones and fax machines can utilize and share the ISDN-based service. While ISDN has had moderate success in various parts of the world, it has largely been surpassed by DSL and cable modems.

Digital Subscriber Line Digital subscriber line (DSL) is a popular way of connecting to the internet. DSL is referred to as a 'last-mile' solution because it is used only for connections from a telephone switching station to a home or office and generally is not used between telephone switching stations.

The abbreviation DSL is used to refer collectively to asymmetric digital subscriber line (ADSL) , symmetric digital subscriber  line  (SDSL) ,  and  other  forms  of  DSL.  DSL  enables more data to be sent over existing copper telephone lines by sending digital pulses in the highfrequency area of telephone wires. Because these high frequencies are not used by normal voice communications, DSL enables your computer to operate simultaneously with voice connections over the same wires. ADSL speeds range from 1.5 to 50 Mbps downstream and up to 16 Mbps upstream. SDSL is said to be symmetric because it supports the same data rates for upstream and downstream traffic (up to 22 Mbps). Like ISDN, ADSL and SDSL require a special modem-like device. As most internet users primarily download content, ADSL is most popular in consumer environments. SDSL is offered primarily to business customers.

Cable Modems In most areas, the company that provides cable television service also provides internet service. With this type of service, a special cable modem is needed to transmit data over cable TV lines. Coaxial cable used for cable TV provides much greater bandwidth than telephone lines, and millions of homes in the United States are already wired for cable TV, so cable modems are a fast, popular method for accessing the internet. Cable modems offer download speeds up to 43 Mbps.

Satellite Connections In many regions of the world, people can only access the internet via satellite, referred to as internet over satellite . These technologies allow users to access the internet via satellites that are placed in a geostationary orbit above the earth's surface. With these services, your PC is connected to a satellite dish hanging on the side of your home or placed on a pole (much like satellite services for your television); you are able to maintain a reliable connection to the satellite in the sky because the satellite orbits the earth at the exact speed of the earth's rotation. Given the vast distance that signals must travel from

the earth up to the satellite and back again, internet over satellites is slower than high-speed terrestrial (i.e., land-based) connections to the internet over copper or fiber-optic cables. In remote regions of the world, however, it is the only option available because installing the cables necessary for an internet connection is not economically feasible or, in many cases, is just not physically possible.

Wireless Broadband Wireless broadband is a technology that is usually found in rural areas where other connectivity options, such as DSL and cable, are not available. A common scenario is that the ISP will install an antenna at a high point, such as a large building or radio tower, and the customer will mount a small dish to the roof and point it at the antenna. Wireless broadband offers speeds similar to DSL and cable and can bridge a distance of up to 50 kilometers (30 miles).

Mobile Wireless Access In addition to the fixed wireless approach, there are also many mobile wireless approaches for connecting to the internet. For example, with a subscription to a data plan, smartphones give you internet access nearly anywhere. Also, special network adapter cards or USB 'dongles' from a cellular service provider allow a notebook computer, tablet, or desktop computer to connect to cellular networks. The advantage of these systems is that, as long as you are in the coverage area of that cell phone provider, you have access to the internet. Most mobile wireless service providers limit the amount of data that can be downloaded per month without incurring expensive fees, making this a relatively expensive option for a person's exclusive method for accessing the internet.

Fiber to the Home Fiber to the home , also known as fiber to the premises , refers to connectivity technology that provides a super-speed connection to people's homes. This is usually done by fiber-optic cabling running directly into new homes. Fiber to the home is currently available only in major metropolitan areas.

Until now, we have talked about ways that individuals typically access the internet. In the following section, we talk more about ways that organizations typically access the internet.

BUSINESS INTERNET CONNECTIVITY. Although home users have enjoyed a consistent increase in bandwidth availability, the demand for corporate use has increased at a greater pace; therefore, the need for faster speeds has become of great importance. In addition to the home connectivity options, business customers also have several high-speed options, described next.

Leased Lines To gain adequate access to the internet, organizations are turning to longdistance carriers to lease dedicated T1 lines for digital transmissions. The T1 line was developed by AT&amp;T as a dedicated digital transmission line that can carry 1.544 Mbps of data. In the United States, companies such as MCI that sell long-distance services are called interexchange carriers because their circuits carry service between the major telephone exchanges. A T1 line usually traverses hundreds or thousands of miles over leased longdistance facilities.

AT&amp;T and other carriers charge as little as US$200 per month for a dedicated T1 circuit. If you need an even faster link, you might choose a T3 line . T3 provides about 45 Mbps of service at about 10 times the cost of leasing a T1 line. Alternatively, organizations often choose to use two or more T1 lines simultaneously rather than jump to the more expensive T3 line. Higher speeds than the T3 are also available but are not typically used for normal business activity. For example, fiber-optic networks offer speeds considerably faster than T3 lines. See Table TB15 for a summary of telecommunication line capacities, including optical carrier (OC) lines that use fiber-optic transmission media.

THE CURRENT STATE OF INTERNET USAGE. The internet is now the most prominent global network. Internet Live Stats (https://www.internetlivestats.com) reports that, as of July 2020, more than 4.6 billion people worldwide had access to the internet. This means that almost 60 percent of the world's population had internet access. One other way to measure the rapid growth of the internet, in addition to the number of users, is to examine the growth in the number of internet hosts -that is, computers working as servers on the internet-as shown in Figure TB30.

## FIGURE TB30

Growth in internet servers (hosts).

Source: Based on http:// www.internetlivestats.com/ total-number-of-websites.

## TABLE TB15 Capacity of Telecommunication Lines

| Type of Line   | Data Rate   |
|----------------|-------------|
| T1             | 1.544 Mbps  |
| T3             | 44.736 Mbps |
| OC-1           | 51.85 Mbps  |
| OC-3           | 155.52 Mbps |
| OC-12          | 622.08 Mbps |
| OC-24          | 1.244 Gbps  |
| OC-48          | 2.488 Gbps  |

## Number of Internet Hosts

<!-- image -->

## Foundational Topics in Database Management

In Chapter 6, you were introduced to database concepts such as attributes, entities, and relationships, as well as managerial aspects related to databases. In the following sections, we delve deeper into the topic of relational database management to give you a better idea of the intricacies involved in designing a sound database.

## Relational Database Design

Much of the work of creating an effective relational database is in the creation of the data model. If the model is not accurate, the database will not be effective. A poor data model will result in data that are inaccurate, redundant, or difficult to search. If the database is relatively small, the effects of a poor design might not be too severe. A corporate database, however, contains many entities, perhaps hundreds or thousands. In this case, the implications of a poor data model can be catastrophic. A poorly organized database is difficult to maintain and process-thus defeating the purpose of having a DBMS in the first place. Undoubtedly, your university maintains databases

<!-- image -->

| Students                                   | Grades                                      |
|--------------------------------------------|---------------------------------------------|
| Student ID Name Campus Address Major Phone | Student ID Course ID Section No. Term Grade |

## Students

| Student ID   | Name         | Campus Address       | Major     | Phone    |
|--------------|--------------|----------------------|-----------|----------|
| 555-39-3232  | Joe Jones    | 123 Any Avenue       | Finance   | 335-2211 |
| 289-42-8776  | Sally Carter | 1200 Wolf Street #12 | Marketing | 335-8702 |

## Grades

| Student ID   | Course ID   |   Section No. | Term   | Grade   |
|--------------|-------------|---------------|--------|---------|
| 555-39-3232  | MIS 250     |             2 | F'15   | D+      |
| 555-39-3232  | MIS 250     |             1 | F'16   | A-      |
| 289-42-8776  | MIS 250     |             3 | S'17   | B+      |

with a variety of entity types-for example, students and grades-with each of these entities having numerous attributes. Attributes of a Student entity might be Student ID, Name, Campus Address, Major, and Phone. Attributes of a Grades entity might include Student ID, Course ID, Section Number, Term, and Grade (see Figure TB31).

For the DBMS to distinguish between records correctly, each instance of an entity must have one unique identifier. For example, each student has a unique Student ID. Note that using the student name (or most other attributes) would not be adequate because students may have the exact same name, live at the same address, or share the same phone number. Consequently, when designing a database, we must always create and use a unique identifier, called a primary key , for each type of entity to store and retrieve data accurately. In some instances, the primary key can also be a combination of two or more attributes, in which case it is called a combination primary key .  An example of this is the Grades entity, shown in Figure TB31, where the combination of Student ID, Course ID, Section Number, and Term can be used to uniquely identify the grade of an individual student in a particular class (section number) in a particular term. Attributes not used as the primary key can be referred to as secondary keys when they are used to identify one or more records within a table that share a common value. For example, a secondary key in the Student entity shown in Figure TB31 would be Major when used to find all students who share a particular major.

ASSOCIATIONS. To retrieve information from a relational database, it is necessary to associate or relate data from separate tables. The three types of relationships (or associations ) among entities are one-to-one, one-to-many, and many-to-many. Table TB16 summarizes each of

TABLE TB16 Rules for Expressing Relationships Among Entities and Their Corresponding Data Structures

| Relationship   | Example                                                                       | Instructions                                                                                                                                                                           |
|----------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One-to-one     | Each team has only one home stadium, and each home stadium has only one team. | Place the primary key from one table (e.g., Stadium) into the other (e.g., Team) as a foreign key.                                                                                     |
| One-to-many    | Each player is on only one team, but each team has many players.              | Place the primary key from the table on the 'one' side of the relationship (e.g., Team) as a foreign key in the table on the 'many' side of the relationship (e.g., Player).           |
| Many-to-many   | Each player participates in many games, and each game has many players.       | Create a third table (e.g., Player Statistics) and place the primary keys from each of the original tables (e.g., Player and Team) together in the third as a combination primary key. |

## FIGURE TB31

The attributes for and links between two entities-students and grades.

## FIGURE TB32

Tables used for storing information about several basketball teams, with no foreign key attributes added; thus, associations cannot be made.

## FIGURE TB33

Tables used for storing information about several basketball teams, with foreign key attributes added to make associations.

## Home Stadium

<!-- image -->

these three associations and shows how they should be handled in database design for a basketball league.

To understand how relationships work, consider Figure TB32, which shows four tablesHome Stadium, Team, Player, and Games-for keeping track of the information for a basketball league. The Home Stadium table lists the Stadium ID, Stadium Name, Capacity, and Location, with the primary key underlined. The Team table contains two attributes, Team ID and Team Name, but nothing about the stadium where the team plays. If we wanted to have such information, we could gain it only by creating a relationship between the Home Stadium and Team tables. For example, if each team has only one home stadium and each home stadium has only one team, we have a one-to-one relationship between the Team and the Home Stadium entities. In situations in which we have one-to-one relationships between entities, we place the primary key from one table in the table for the other entity and refer to this attribute as a foreign key . In other words, a foreign key refers to an attribute that appears as a non-primary key attribute in one entity and as a primary key attribute (or part of a primary key) in another entity. By sharing this common-but unique-value, entities can be associated, or linked together. We can choose in which of these tables to place the foreign key of the other. After adding the primary key of the Home Stadium entity to the Team entity, we can identify which stadium is the home for a particular team and then be able to find all the details about that stadium (see section A in Figure TB33).

When we find a one-to-many relationship-for example, each player plays for only one team, but each team has many players-we place the primary key from the entity on the 'one' side of the relationship, the Team entity, as a foreign key in the table for the entity on the 'many' side of the relationship, the Player entity (see section B in Figure TB33). In essence, we take from the one and give to the many, a Robin Hood strategy.

When we find a many-to-many relationship (e.g., each player plays in many games, and each game has many players), we create a third (new) entity-in this case, the Player Statistics entity and corresponding table. We then place the primary keys from each of the original entities together into the third (new) table as a combination primary key (see section C in Figure TB33).

- A. One-to-one relationship: Each team has only one home stadium, and each home stadium has only one team.

## Team

Team ID

Stadium ID

Team Name

- B. One-to-many relationship: Each player is on only one team, but each team has many players.

## Player

Player ID

Team ID

Player Name

Position

- C. Many-to-many relationship: Each player participates in many games, and each game has many players.

Player Statistics

Team 1

Team 2

Date

Player ID

Points

Minutes

Fouls

You may have noticed that by placing the primary key from one entity in the table of another entity, we are creating a bit of redundancy. We are repeating the data in different places. We are willing to live with this bit of redundancy, however, because it enables us to keep track of the interrelationships  among  the  many  pieces  of  important  organizational  data  that  are  stored  in different tables. By keeping track of these relationships, we can quickly answer questions such as 'Which players on the Wildcats played in the game on February 16 and scored more than 10 points?' In a business setting, the question might be 'Which customers purchased a 2020 Toyota Prius from a salesperson named Jeff at the Desert Toyota dealership in Tucson, Arizona, during the first quarter of 2020, and how much did each customer pay?' This kind of question would be useful in calculating the bonus money Jeff should receive for that quarter or in contacting the owners of those specific vehicles in the event of a recall by the manufacturer.

ENTITY-RELATIONSHIP DIAGRAMMING. A diagramming technique that creates an entityrelationship diagram (ERD) is commonly used when designing relational databases, especially when showing associations between entities. To create an ERD, you draw entities as boxes and draw lines between entities to show relationships. Each relationship can be labeled on the diagram to give it additional meaning. For example, Figure TB34 shows an ERD for the basketball league data previously discussed. From this diagram, you can see the following associations:

- ■ Each Home Stadium has a Team.
- ■ Each Team has Players.
- ■ Each Team participates in Games.
- ■ For each Player and Game, there are Game Statistics.

When you are designing a complex database, with numerous entities and relationships, ERDs are very useful. They allow the designer to talk with people throughout the organization to make sure that all entities and relationships have been found.

THE RELATIONAL MODEL. Now that we have discussed associations and data models, we need a mechanism for joining entities that have natural relationships with one another. For example, in the University database we described previously, there are several relationships among the four entities: students, instructors, classes, and grades. Students are enrolled in multiple classes. Likewise, instructors teach multiple classes and have many students in their classes in a semester. At the end of the semester, instructors assign a grade to each student, and each student earns grades in multiple classes. It is important to keep track of these relationships. We might, for example, want to know which courses a student is enrolled in so that we can notify her instructors that she will miss classes because of an illness. The primary DBMS approach, or model, for keeping track of these relationships among data entities is the relational model. Other models-the hierarchical, network, and object-oriented models-are also used to join entities within commercial DBMSs, but this is beyond the scope of our discussion (see Hoffer, Ramesh, &amp; Topi, 2019).

The most common DBMS approach in use today is the relational database model .  A DBMS package using this approach is referred to as a relational DBMS. With this approach, the DBMS views and presents entities as two-dimensional tables, with records as rows and attributes as columns. Tables can be joined when there are common columns in the tables. The uniqueness of the primary key, as mentioned earlier, tells the DBMS which records should be joined with others in the corresponding tables. This structure supports very powerful data manipulation capabilities and linking of interrelated data. Database files in the relational model are three-dimensional: a table has rows (one dimension) and columns (a second dimension) and can contain rows of

<!-- image -->

## FIGURE TB34

An entity-relationship diagram showing the relationships between entities in a basketball league database.

## FIGURE TB35

With the relational model, we represent these two entities, department and instructor, as two separate tables and capture the relationship between them with a common column in each table.

## FIGURE TB36

Database of students, courses, instructors, and grades with redundant data. Source: Microsoft access for Microsoft 365, Windows 10,

Microsoft Corporation.

## Department Records

| Dept No   | Dept Name   | Location   | Dean   |
|-----------|-------------|------------|--------|
| Dept A    |             |            |        |
| Dept B    |             |            |        |
| Dept C    |             |            |        |

## Instructor Records

| Instructor No   | Inst Name   | Title   | Salary   | Dept No   |
|-----------------|-------------|---------|----------|-----------|
| Inst 1          |             |         |          |           |
| Inst 2          |             |         |          |           |
| Inst 3          |             |         |          |           |
| Inst 4          |             |         |          |           |

attributes in common with another table (a third dimension). This three-dimensional database is potentially much more powerful and useful than traditional, two-dimensional, 'flat-file' databases (see Figure TB35).

A good relational database design eliminates unnecessary data duplications and is easy to maintain. To design a database with clear, non-redundant relationships, you perform a process called normalization.

NORMALIZATION. To be effective, databases must be efficient. Developed in the 1970s, normalization is a technique to make complex relational databases more efficient and more easily handled by the DBMS (Hoffer et al., 2019). Normalization makes sure that each table contains only attributes that are related to the entity; hence, normalization helps to eliminate data duplication. To understand the normalization process, let us return to the scenario in the beginning of this section. Think about your report card. It looks like nearly any other report or invoice. Your personal data are usually at the top, and each of your classes is listed, along with an instructor, a class day and time, the number of credit hours, and a location. Now think about how these data are stored in a relational database. Imagine that this database is organized so that in each row of the database, the student's identification number is listed on the far left. To the right of the student ID are the student's name, local address, major, phone number, course and instructor information, and a final course grade (see Figure TB36). Notice that there are redundant data for students, courses, and instructors in each row of this database. This redundancy means that this database is not well organized. If, for example, we want to change the phone number of an instructor who has hundreds of students, we must change this number hundreds of times. In addition, this redundancy wastes storage space.

<!-- image -->

<!-- image -->

Elimination of data redundancy is a major goal and benefit of using data normalization techniques. After the normalization process, the student data are organized into five separate tables (see Figure TB37). This reorganization helps simplify the ongoing use and maintenance of the database and any associated analysis programs.

## Advanced Database Models

One of the problems with relational databases is that their performance degrades rapidly after getting very large. Relational databases are very efficient when processing highly structured data, but perform very poorly when processing unstructured data. Unstructured data refers to data that do not have an identifiable structure. Unstructured data are typically text-heavy, but may contain data such as dates, numbers, or even different types of media. This results in irregularities that make it difficult to utilize traditional database and processing approaches. In the world of Big Data, the relational model has been found to be less than optimal for storing and processing massive amounts of unstructured data. Companies such as Amazon, Facebook, and Google are storing and processing many petabytes of unstructured data daily. The most prevalent data model for storing Big Data is NoSQL ('not only SQL'-referring to nonrelational databases).

Large scale NoSQL databases, such as Hadoop often are processed on computer clusters. A computer cluster consists of a set of computers that work together as a single system. Hadoop is an open source programming environment for processing NoSQL databases. Thus, a Hadoop cluster is a computer cluster designed for storing and analyzing huge amounts of unstructured data that is stored in a NoSQL database. In addition to Hadoop, there are many other NoSQL databases, including Cassandra, Hypertable, DynamoDB, IBM Informix, and others. NoSQL is the foundation of most social media platforms. Being able to process massive amounts of unstructured data is fundamental to virtually all Big Data applications.

## Key Points Review

1. Discuss foundational information systems (IS) hardware concepts. IS hardware is classified into three types: input, processing, and output technologies. Input hardware consists of devices used to enter data into a computer. Processing hardware transforms inputs into outputs. The CPU is the device that performs this transformation, with the help of several other closely related devices that store and recall data. Data are stored on primary and secondary storage devices. Finally, output-related hardware focuses on delivering information in a usable format to users.
2. Describe foundational topics related to system software, programming languages, and application development environments. System software, or the operating system, performs many different tasks, such as booting your computer, reading programs into memory, managing memory allocation to those programs, managing where programs and files are located in secondary storage, maintaining the structure of directories and subdirectories, etc. A programming language is the computer language that programmers use to write application programs.

## FIGURE TB37

Organization of information on students, courses, instructors, and grades after normalization. Source: Microsoft access for Microsoft 365, Windows 10, Microsoft Corporation.

- To run on a computer, a programs' source code must be translated into binary machine language through special types of programs, called compilers and interpreters. Object-oriented programming, visual programming, and web development languages complement traditional programming languages. Finally, CASE environments help systems developers construct large-scale systems more rapidly and with higher quality.
3. Describe foundational networking and internet concepts. Networks provide for services such as transmitting files, sharing printers, or sending and receiving messages. There are several types of computer networks, classified according to their use and distance covered. To enable rapid transmission of massive amounts of data, most data networks rely on packet switching. Protocols are agreed-on formats for transmitting data between connected computers; the most prominent standards are TCP/IP and Ethernet. Networks exchange data by using cable or wireless transmission media, and media access control refers to the rules that govern how a given workstation

gains access to the transmission media. The shape of a network can vary; the four most common topologies are star, ring, bus, and mesh configurations. The internet is composed of networks that are developed and maintained by many different entities. It follows a hierarchical structure; high-speed central networks called backbones are like interstate highways, enabling traffic from midlevel networks to get on and off. Routers are used to interconnect independent networks.

4. Explain foundational database management concepts. To get the most of their data, organizations must take care to create an accurate data model. Often, entity-relationship diagrams are used when designing relational databases. A primary key is used to uniquely identify records in a database. A foreign key is used to link entities together. A useful diagramming technique is entity-relationship diagramming, displaying entities and the associations between them. Normalization is used to reduce redundancy in a database. Nonrelational databases are used for handling large amounts of unstructured data.

## Key Terms

## Foundational Hardware Key Terms

| American Standard Code for Informa- tion Interchange (ASCII) 481 arithmetic logic unit (ALU) 480 audio 478    |
|---------------------------------------------------------------------------------------------------------------|
| basic input/output system (BIOS) 482                                                                          |
| batch data 477                                                                                                |
| batch processing 477                                                                                          |
| binary code 481 bit 481                                                                                       |
| byte 481                                                                                                      |
| bytes per inch (BPI) 483                                                                                      |
| cache 482 cathode ray tube (CRT) 485                                                                          |
| CD-R (compact disc-recordable) 483 CD-RW (compact                                                             |
| disc-rewritable) 483 central processing unit (CPU) 480 characters per inch 483 clock speed 481 clock tick 481 |
| control unit 480 density 483                                                                                  |
| digital video disc 483                                                                                        |
| digitize 481 DVD-ROM (digital                                                                                 |
| versatile disc-read-only memory)                                                                              |
| flash drive 483                                                                                               |
| 483                                                                                                           |

| smart card 478 solid-state drive (SSD) 482 speech recognition 478 streaming audio 479 streaming media 479 streaming video 479   |
|---------------------------------------------------------------------------------------------------------------------------------|
| system clock 481                                                                                                                |
| touch screen 485                                                                                                                |
| tape 483                                                                                                                        |
| recognition software 477                                                                                                        |
| text                                                                                                                            |
| Unicode 481                                                                                                                     |
| video 478                                                                                                                       |
| voice-to-text software 478                                                                                                      |
| volatile memory 482                                                                                                             |

## Foundational Software Key Terms

applet 490 cascading style sheets (CSS) 489 compiler 487 computer-aided software engineering (CASE) 491 executable 487 graphical user interface (GUI) 487 HTML editor 489 HTML tag 489 interpreter 487 Java 490 JavaScript 490 Microsoft.NET 490 object-oriented language 487

| scripting language 490 source code 486 utilities 486 utility program 486   |     |
|----------------------------------------------------------------------------|-----|
| visual programming language web page builder 489                           | 487 |

## Foundational Networking Key

## Terms

| Advanced Research Projects Agency Network (ARPANET) 506 analog signals 509 asymmetric digital subscriber line (ADSL) 510 authentication service 494   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| backbone 503 Bluetooth 495                                                                                                                            |
| bus network 500                                                                                                                                       |
| cable modem 510                                                                                                                                       |
| carrier sense multiple access/collision avoidance (CSMA/CA) 500                                                                                       |
| cell 503 cellular phone 503 centralized computing 492                                                                                                 |
| collaborative computing 493 Defense Advanced Research Projects                                                                                        |
| Agency (DARPA) 506 digital signals 509 digital subscriber line (DSL) 510 directory service 494                                                        |
| distributed computing 493                                                                                                                             |
| Domain Name System (DNS) 508                                                                                                                          |

| enterpriseWAN 495 498                                                                                              |
|--------------------------------------------------------------------------------------------------------------------|
| Ethernet fiber to the home 511 fiber to the premises 511 global network 495 integrated services digital (ISDN) 509 |
| network interexchange carrier 511                                                                                  |
| Internet Corporation for Assigned Names and Numbers 508                                                            |
| internet exchange point (IXP) 509 internet host 511 internet over satellite 510                                    |
| internet service provider (ISP) 508 InterNIC 508 IP 498                                                            |
| IP datagram 498 IPv6 508 media access control 500 mesh network 500 mobile wireless 511                             |
| modem 509 National Science Foundation (NSF) 506                                                                    |
| National Science Foundation Network (NSFNET) 506                                                                   |
| network interface card 499 network topology 499                                                                    |
| Open Systems Interconnection model 497                                                                             |
| (OSI) packet switching 496                                                                                         |

## Review Questions

## Foundational Hardware Review Questions

| TB-1.                                  | IS hardware is classified into what three major types?                           |
|----------------------------------------|----------------------------------------------------------------------------------|
| TB-2.                                  | Describe various methods for entering data into and interacting with a computer. |
| TB-3.                                  | How do computers represent data internally?                                      |
| TB-4.                                  | Describe the role of a motherboard.                                              |
| TB-5.                                  | What determines the speed of a CPU?                                              |
| TB-6.                                  | Compare and contrast the different types of secondary data storage.              |
| TB-7.                                  | What are output devices? Describe various methods for providing computer output. |
| Foundational Software Review Questions | Foundational Software Review Questions                                           |
| TB-8.                                  | Define the term software and list several software packages and their uses.      |
| TB-9.                                  | Describe at least four different tasks performed by an operating system.         |

| TB-10.                                   | Describe the similarities and differences between at least two major operating systems in use today.   |
|------------------------------------------|--------------------------------------------------------------------------------------------------------|
| TB-11.                                   | Name and describe four functions of utility programs.                                                  |
| TB-12.                                   | Name and describe the five important concepts of object-oriented programming.                          |
| TB-13.                                   | What is HTML, and why is it important?                                                                 |
| TB-14.                                   | Describe various options for adding dynamic content to a web page.                                     |
| TB-15.                                   | What is CASE, and how can it help in the development of information systems?                           |
| Foundational Networking Review Questions | Foundational Networking Review Questions                                                               |
| TB-16.                                   | How are LANs, WANs, and global networks related to each other?                                         |
| TB-17.                                   | What are the roles of authentication services and directory services?                                  |

| plain old telephone service                                                            | plain old telephone service                                                            | plain old telephone service                                                            |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| propagation delay 505                                                                  | propagation delay 505                                                                  | propagation delay 505                                                                  |
| public switched telephone network                                                      | public switched telephone network                                                      | public switched telephone network                                                      |
| (PSTN)                                                                                 | (PSTN)                                                                                 | 509                                                                                    |
| ring network 500 router 498                                                            | ring network 500 router 498                                                            | ring network 500 router 498                                                            |
| star network 499                                                                       | star network 499                                                                       | star network 499                                                                       |
| symmetric digital subscriber line                                                      | symmetric digital subscriber line                                                      | symmetric digital subscriber line                                                      |
| T1 line                                                                                | 511                                                                                    | 511                                                                                    |
| T3 line                                                                                | 511                                                                                    | 511                                                                                    |
| TCP                                                                                    |                                                                                        |                                                                                        |
| 498                                                                                    | 498                                                                                    | 498                                                                                    |
| terminal 492 value-added network 495                                                   | terminal 492 value-added network 495                                                   | terminal 492 value-added network 495                                                   |
| wireless access point 501                                                              | wireless access point 501                                                              | wireless access point 501                                                              |
| wireless broadband 511 wireless controller 501                                         | wireless broadband 511 wireless controller 501                                         | wireless broadband 511 wireless controller 501                                         |
| computer cluster 517 combination primary key 513 entity-relationship diagram (ERD) 515 | computer cluster 517 combination primary key 513 entity-relationship diagram (ERD) 515 | computer cluster 517 combination primary key 513 entity-relationship diagram (ERD) 515 |
| foreign key 514                                                                        | foreign key 514                                                                        | foreign key 514                                                                        |
| primary key 513                                                                        | primary key 513                                                                        | primary key 513                                                                        |
| relational database model 515                                                          | relational database model 515                                                          | relational database model 515                                                          |
| relationship 513                                                                       | relationship 513                                                                       | relationship 513                                                                       |
| secondary key 513                                                                      | secondary key 513                                                                      | secondary key 513                                                                      |
| normalization 516                                                                      | normalization 516                                                                      | normalization 516                                                                      |

TB-18. What is packet switching, and why is it useful?

TB-19.

What is the purpose of the OSI model?

TB-20.

What is a network topology? Describe the four basic topologies.

TB-21.

What are three common types of transmission media that use cabling?

TB-22.

What are four common methods of wireless transmission media for networking, and how do they differ from each other?

TB-23.

What is the internet, and why was it created?

TB-24.

Other than dial-up, what are three   alternatives for connecting to the internet at home?

## Self-Study Questions

## Foundational Hardware Self-Study Questions

TB-32.

All of the following are considered primary storage except \_\_\_\_\_\_\_\_\_\_\_\_\_\_.

A. SSDs

B. RAM

C. registers

D. cache

TB-33.

Which of the following is not an input device?

A. biometric scanner

B. touch screen

C. LCD screen

D. barcode reader

TB-34.

Which of the following is an output device?

A. cathode ray tube

B. scanner

C. video camera

D. keyboard

TB-35.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_ can convert handwritten text into

computer-based characters.

A. Scanners

B. Bar code/optical character readers

C. Text recognition software

D. Audio/video

TB-36.

A \_\_\_\_\_\_\_\_\_\_\_\_\_\_ card is a special credit card with a microprocessor chip and memory circuits.

A. smart

B.

master

C. universal

D. proprietary

Answers are on page 523.

## Foundational Software Self-Study Questions

TB-37.

An operating system performs which of the

following tasks?

A. booting the computer

B. managing where programs and files are stored

C. sending documents to the printer

D. all of the above

## Foundational Database Review Questions

TB-25.

Describe why database design is important for modern organizations.

TB-26.

Compare and contrast the primary key, combination key, and foreign key within an entity.

TB-27.

Describe the three types of relationships in a relational database.

TB-28. What is the purpose of a secondary key? What is an entity-relationship diagram, and

TB-29. why is it useful?

TB-30. What is the relational model?

TB-31. Why is redundancy undesired?

TB-38. What is the name of the programming language developed by Sun Microsystems in the 1990s?

A. Latte

B. Java

C. Mocha

D. none of the above

TB-39.

Which of the following programming languages would most likely not be used for building web applications?

A. HTML

B. JavaScript

C. PHP

D. Fortran

TB-40.

A utility program may provide \_\_\_\_\_\_\_\_\_\_\_\_\_\_.

A. antivirus protection

B. file conversion capability

C. file compression and defragmentation

D. all of the above

TB-41.

CASE tools support all of the following except:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_.

A. diagramming

B. consistency checking

C. generating code

D. compiling code

Answers are on page 523.

## Foundational Networking Self-Study Questions

TB-42.

Which of the following is not a type of cable medium?

A. twisted pair

B. coaxial

C. fiber-optic

D. shielded pair

TB-43.

All of the following are common applications

of high-frequency radio communication except

\_\_\_\_\_\_\_\_\_\_\_\_\_\_.

A. police radios

B. cellular phones

C. microwave transmission

D. facsimiles

TB-44. Which of the following is the protocol of the inter- net, allowing different interconnected networks to communicate using the same language?

- A. Ethernet

- B. C++

- C. TCP/IP

D. router

TB-45.

Which is the fastest connection available for home users?

A. dial-up

B. DSL

- C. wireless broadband

- D. fiber to the home

TB-46.

Which of the following is a typical way large corporations connect to the internet?

A. satellite

B. cable

C. T1 lines

D. all of the above

Answers are on page 523.

## Foundational Database Self-Study Questions

TB-47.

A(n) \_\_\_\_\_\_\_\_\_\_\_\_\_\_ is a unique identifier that can be a combination of one or more attributes.

- A. secondary key

- B. primary key

- C. tertiary key

- D. elementary key

## Problems and Exercises

## Foundational Hardware Problems and Exercises

TB-52. Match the following terms with the appropriate definitions:

- i.  Motherboard
- ii.  Audio
- iii.  DVD-ROM
- iv.  Smart card
- v.  Streaming video
- a.  Analog or digital sound data
- b.  A special credit card-sized card containing a microprocessor chip, memory circuits, and often a magnetic stripe
- c.  An optical storage device that has more storage space than a CD-ROM disk and uses a shorterwavelength laser beam, which allows more optical pits to be deposited on the disk
- d.  A sequence of moving images, sent in a compressed form over the internet and displayed on the receiver's screen as the images arrive
- e.  A large printed plastic or fiberglass circuit board that contains all the components that do the actual processing work of the computer and

- TB-48. Which of the following is not true in regard to the relational database model?

- A. Entities are viewed as tables, with records as rows and attributes as columns.

- B. Databases use keys and redundant data in different tables to link interrelated data.

- C. Entities are viewed as children of higher-level attributes.

- D. A properly designed table has a unique identifier that may consist of one or more attributes.

TB-49.

Each team has only one home stadium, and each home stadium has only one team. This is an example of which of the following relationships?

- A. one-to-one

- B. one-to-many

- C. many-to-many

- D. many-to-one

TB-50.

A popular diagramming technique for designing databases is called \_\_\_\_\_\_\_\_\_\_\_\_\_\_.

- A. flowcharting

- B. database diagramming

- C. entity-relationship diagramming

- D. none of the above

TB-51.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_ is a technique to make a complex

database more efficient by eliminating redundancy.

- A. Extraction, transformation, and loading (ETL)

- B. Associating

- C. Normalization

- D. Standardization

Answers are on page 523.

holds or connects to all the computer's electronic components

TB-53.

Visit a computer shop or look on the web for trackballs or touch pads. What is new about how these input devices look or how they are used? What are some of the advantages and disadvantages of each device?

TB-54. What types of printers are most common today? What is the cost of a color printer versus a blackand-white one? Compare and contrast laser and ink-jet printers in terms of speed, cost, and quality of output. What kind of printer would you buy or have you bought?

TB-55. Based on your experiences with different input devices, which do you like the best and least? Why? Are your preferences due to the devices' design or usability, or are they based on the integration of the device with the entire information system?

TB-56.

Choose a few of the computer hardware vendors that sell computers to the general public. These include Dell, HP, Lenovo, Apple, and many lesser-known brands. Using each company's website, determine what options these vendors provide for input devices, processing devices, and

output devices. Does it seem that this company has a broad range of choices for its customers? Is there something that you did not find available from this company? Present your findings in a 10-minute presentation to the rest of the class.

## Foundational Software Problems and Exercises

TB-57. Match the following terms with the appropriate definitions:

- i.  Applet
- ii.  Visual programming language
- iii.  Scripting language
- iv.  Interpreter
- v.  Compiler
- a.  A software program that translates an entire program's source code into machine language that can be read and executed directly by the computer
- b.  A programming language that provides a graphical user interface and is generally easier to use than non-GUI languages
- c.  A program designed to be executed within another application (such as a web page)
- d.  A software program that translates a programming language into machine language one statement at a time
- e.  A programming language for integrating interactive components into a web page

TB-58. What are the implications for an organization of using more than one operating system? What might be the advantages? What are some of the disadvantages? Would you recommend such a situation? Present a 10-minute briefing to the rest of the class on your findings.

TB-59.

Visit the website of your favorite online retailer. Which parts of the content are created dynamically? What interactive components do the different web pages include? Do different types of pages (e.g., home page or payment and shipping page) need different types of interactive components?

TB-60. Based on your own experiences with computers and computer systems, what do you like and dislike about different operating systems that you have used? Were these uses on a professional or a personal level or both? Who made the decision to purchase that particular operating system? Did you have any say in the purchase decision?

- TB-61. Imagine that you and a friend are at a local ATM getting some cash from your account to pay for a movie. The ATM does not seem to be working. It is giving you an error message every time you press any button. Is this most likely a software-related problem, a hardware-related problem, or a networkrelated problem? Why? Use the information in this and other briefings to help you make this assessment.

## Foundational Networking Problems and Exercises

TB-62.

Match the following terms with the appropriate definitions:

- i.  Protocols
- ii.  Ethernet
- iii.  FTTH
- iv.  T1 line
- v.  Wireless access point
- a.  A dedicated digital transmission line that can carry 1.544 Mbps of information
- b.  A networking device that transmits and receives wireless signals to allow wireless devices to connect to the network
- c.  High-speed network connectivity to homes and offices that is implemented using fiber-optic cable
- d.  The most widely used local area network protocol, supporting data rates of up to 100 gigabits per second
- e.  The procedures that different computers follow when they transmit and receive data

Discuss the difference between PBX networks and LANs. What are the advantages of each? What are possible disadvantages of each? When would you recommend one over the other?

Personal area networks using Bluetooth have become very popular. Visit https://www.bluetooth .com and investigate the different use cases of this wireless technology. Select three use cases that you find interesting and prepare a 10-minute presentation on what these are and how Bluetooth is used in their context.

Describe one of your experiences with a computer network. What type of topology was being used? Was the network connected to any other networks? How?

TB-63.

TB-64.

TB-65.

TB-66.

Working in a group, have everyone describe what type of network would be most appropriate for a small office with about 10 computers, one printer, and one scanner, all within one floor in one building and relatively close to one another. Be sure to talk about transmission media, network topology, and hardware. Did all group members come up with the same option? Why or why not? What else would you need to know to make a good recommendation?

TB-67. Investigate the options for high-speed, broadband internet access into your home. What options are available to you, and how much do they cost?

TB-68.

You have probably experienced several different types of connection-from the university T1 connections to a home DSL or even dial-up connection. If you had to balance between cost and speed, which connection would you choose?

TB-69. Explain in simple language how the internet works. Be sure to talk about backbones, packet switching, networks, routers, TCP/IP, and internet services. What technologies, hardware, and software do you utilize when using the internet? What would you like to use that isn't available to you?

## Foundational Database Problems and Exercises

TB-70. Match the following terms with the appropriate definitions:

- i.  Primary key
- ii.  Foreign key
- iii.  Relational database model
- iv.  Relationship
- v.  Secondary key
- a.  Attribute not used as the primary key that can be used to identify one or more records within a table that share a common value
- b.  An attribute that appears as a nonprimary key attribute in one entity and as a primary key in another
- c.  A field included in a database table that ensures that each instance of an entity is stored or retrieved accurately
- d.  An association between entities in a database to enable data retrieval
- e.  A data management approach in which entities are presented as two-dimensional tables that can be joined together with common columns
11. TB-71. You see an announcement for a job as a database administrator for a large corporation but are unclear about what this title means. Research this on the web and obtain a specific job announcement.
12. TB-72. Why would it matter what data type is used for the attributes within a database? How does this relate to programming? How does this relate to queries and calculations? Does the size of the database matter?

TB-73. Have several classmates interview database administrators within organizations with which they are familiar. To whom do these people report? How many employees report to these people? Is there a big variance in the responsibilities across organizations? Why or why not?

TB-74.

Based on your understanding of a primary key and the information in the following sample grades table, determine the best choice of attribute(s) for a primary key.

|   Student ID | Course              | Grade   |
|--------------|---------------------|---------|
|       100013 | Visual Programming  | A       |
|       000117 | Telecommunications  | A       |
|       000117 | Introduction to MIS | A       |

TB-75. Search the web for an organization with a web page that utilizes a link between the web page and the organization's own database. Describe the data that the user enters and the organization's possible uses for these data. Can you retrieve company information, or can you only send information to the company? How are the data displayed on the web page?

| Answers to the Foundational Hardware Self-Study Questions   | Answers to the Foundational Hardware Self-Study Questions   | Answers to the Foundational Hardware Self-Study Questions   | Answers to the Foundational Hardware Self-Study Questions   | Answers to the Foundational Hardware Self-Study Questions   |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| TB-32. A, p. 482                                            | TB-33. C, p. 485                                            | TB-34. A, p. 485                                            | TB-35. C, p. 477                                            | TB-36. A, p. 478                                            |
| Answers to the Foundational Software Self-Study Questions   | Answers to the Foundational Software Self-Study Questions   | Answers to the Foundational Software Self-Study Questions   | Answers to the Foundational Software Self-Study Questions   | Answers to the Foundational Software Self-Study Questions   |
| TB-37. D, p. 485                                            | TB-38. B, p. 488                                            | TB-39. D, p. 488                                            | TB-40. D, p. 486                                            | TB-41. D, p. 491                                            |
| Answers to the Foundational Networking Self-Study Questions | Answers to the Foundational Networking Self-Study Questions | Answers to the Foundational Networking Self-Study Questions | Answers to the Foundational Networking Self-Study Questions | Answers to the Foundational Networking Self-Study Questions |
| TB-42. D, p. 501                                            | TB-43. D, p. 503                                            | TB-44. C, p. 498                                            | TB-45. D, p. 511                                            | TB-46. C, p. 511                                            |
| Answers to the Foundational Database Self-Study Questions   | Answers to the Foundational Database Self-Study Questions   | Answers to the Foundational Database Self-Study Questions   | Answers to the Foundational Database Self-Study Questions   | Answers to the Foundational Database Self-Study Questions   |
| TB-47. B, p. 513                                            | TB-48. C, p. 512                                            | TB-49. A, p. 513                                            | TB-50. C, p. 515                                            | TB-51. C, p. 516                                            |

## References

Evans, A., Martin, K., &amp; Poatsy, M.A. (2020). Technology in Action Complete (16th ed.). Boston, MA: Pearson.

- Hoffer, J., Ramesh, V., &amp; Topi, H. (2019). Modern database management (13th ed.). Boston, MA: Pearson.

Panko, R., &amp; Panko, J. (2019). Business data networks and security (11th ed.). Boston, MA: Pearson.

Sharma, B. (2020). Top 15 sensor types being used most by IoT application development companies. Finoit . Retrieved July 8, 2020, from https://www.finoit.com/blog/top-15-sensor-typesused-iot

- Stallings, W. (2020). Cryptography and network security: Principles and practice (8th ed.). Boston, MA: Pearson.
- Tanenbaum, A., Feamster, N., &amp; Wetherall, D. (2021). Computer networks (6th ed.). Boston, MA: Pearson.
- Te'eni, D., Carey, J. M., &amp; Zhang, P. (2007). Human-computer interaction: Developing effective organizational information systems . New York: Wiley.
- Valacich, J. S., &amp; George, J. F. (2020). Modern systems analysis and design (9th ed.). Boston, MA: Pearson.