// -*- c++ -*-
// Copyright @ 2002-2009, Cognitec Systems AG 
// All rights reserved.
//
//


//#include "/opt/FVSDK_9_4_0/include/FRsdk/cbeff.h"
//#include "/opt/FVSDK_9_4_0/include/FRsdk/config.h"
//#include <FRsdk/eyes.h>
//#include "/opt/FVSDK_9_4_0/include/FRsdk/jpeg.h>"

// support for jpeg2000 images
//#define J2K_SUPPORTED

//#if defined( FRSDK_ARM_EABI)
//#undef J2K_SUPPORTED
//#endif

//#if defined( J2K_SUPPORTED)
//#include <FRsdk/j2k.h>
//#endif

//#include <opt/FVSDK_9_4_0/include/FRsdk/bmp.h>
//#include <FRsdk/png.h>
//#include <FRsdk/pgm.h>
#include "/opt/FVSDK_9_4_0/include/FRsdk/portrait.h"
#include <FRsdk/portraittests.h>
#include <FRsdk/tokenface.h>

#include "cmdline.h"

#include <cmath>
#include <cstdlib>

#include <sstream>
#include <fstream>
#include <exception>

using namespace std;
using namespace FRsdk;

ostream& operator<<( ostream& o, const FRsdk::Position& p) {
  o << " [ " << p.x() << " , " << p.y() << " ] ";
  return o;
}

ostream& operator<<( ostream& o, const FRsdk::Portrait::Characteristics& pc){
  o << "\t age(): " << pc.age() << endl;
  return o;
}

int usage()
{
  cerr << "usage: acquisition -cfg <config file> -img <image file> " 
       << "[ -cbeff <cbeff file> [ -token <token file>]]" << endl
       << "[-mineye <relative minimal eye distance>]" << endl
       << "[-maxeye <relative maximal eye distance>]" << endl
       << "\tconfig file   ... frsdk configuration file" << endl
       << "\timage file    ... an image source file name (BMP, JPEG, JPEG2000, PGM or PNG format)" << endl
       << "\tcbeff file    ... a cbeff destination file name" << endl
       << "\ttoken file    ... a token face image destination file name (PNG format)"
       << endl 
       << "\trelative minimal eye distance ... the minimal eye distance to look for, relative to image width, default: 0.1" << endl
       << "\trelative maximal eye distance ... the maximal eye distance to look for, relative to image width, default: 0.4" << endl << endl;
  return 1;
}

int main( int argc, const char* argv[] )
{
  try {
    FRsdk::CmdLine cmd( argc, argv);
    if( cmd.hasflag("-h")) return usage();
    if( !cmd.getspaceflag("-cfg")) return usage();
    if( !cmd.getspaceflag("-img")) return usage();


    // initialize and resource allocation
    ifstream configIStream( cmd.getspaceflag("-cfg"), ios::in);
    FRsdk::Configuration cfg( configIStream);

    FRsdk::Face::Finder faceFinder( cfg);
    //FRsdk::Eyes::Finder eyesFinder( cfg);
    FRsdk::Portrait::Analyzer portraitAnalyzer( cfg);
    //FRsdk::ISO_19794_5::FullFrontal::Test iso19794Test( cfg);
    //FRsdk::Portrait::Feature::Test featureTest( cfg);
    //FRsdk::ISO_19794_5::TokenFace::Creator tfcreator( cfg);

    FRsdk::CountedPtr<FRsdk::Image> img;

    // try opening jpg image
    try {
      img = new FRsdk::Image
        ( FRsdk::Jpeg::load
          ( string ( cmd.getspaceflag("-img")), 
            FRsdk::ImageIO::PropertiesFeedback( new ImageCoutFeedback)));
    }
    catch (exception& e) {}
    // try opening bmp image
    if (img == 0) try {
      img = new FRsdk::Image
        ( FRsdk::Bmp::load
          ( string( cmd.getspaceflag("-img")), 
            FRsdk::ImageIO::PropertiesFeedback( new ImageCoutFeedback)));
    }
    catch (exception& e) {}
    // try opening pgm/ppm image
    if (img == 0) try {
      img = new FRsdk::Image
        ( FRsdk::Pgm::load
          ( string( cmd.getspaceflag("-img")), 
            FRsdk::ImageIO::PropertiesFeedback( new ImageCoutFeedback)));
    }
    catch (exception& e) {}
    // try opening png file
    if (img == 0) try {
      std::ifstream pngFile;
      pngFile.open( cmd.getspaceflag("-img"), ios::binary);
      img = new FRsdk::Image
        ( FRsdk::Png::load
          ( pngFile, 
            FRsdk::ImageIO::PropertiesFeedback( new ImageCoutFeedback)));
    }
    catch (exception& e) {}
    if (img == 0) 
      cout << "<image file> contains no recognized image file format" 
	   << endl;

    // doing face finding
    FRsdk::Face::LocationSet faceLocations = 
      faceFinder.find (*img, mindist, maxdist);

    if( faceLocations.size() < 1) {
      throw AcquisitionError( "Unable to locate face");
    } else {
      const FRsdk::Face::Location& l = faceLocations.front();
      cout << "Found face: " << confidence=" << l.confidence << endl;
    }
  }
  catch( const FRsdk::FeatureDisabled& e) {
    cout << "Feature not enabled: " << e.what() << endl;
    return EXIT_FAILURE;
  }  
  catch( const FRsdk::LicenseSignatureMismatch& e) {
    cout << "License violation: " << e.what() << endl;
    return EXIT_FAILURE;
  }
  catch( const AcquisitionError& e) {
    cout << "Acquisition Error: " << e.what() << endl;
    return EXIT_SUCCESS;
  }
  catch( exception& e) {
    cout << e.what() << endl;
    return EXIT_FAILURE;
  }
  catch( ... ) {
#ifdef UNDER_CE
    printMemoryStatus( "Characteristics: " );
#endif
    cout << "caught unknown exception"  << endl;
    return EXIT_FAILURE;
  }
  
  return EXIT_SUCCESS;
}
