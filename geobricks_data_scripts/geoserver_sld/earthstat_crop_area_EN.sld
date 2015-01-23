<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc"
  xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd">
  <NamedLayer>
    <Name>rain</Name>
    <UserStyle>
      <Name>rain</Name>
      <Title>Rain distribution</Title>
      <FeatureTypeStyle>
        <Rule>
          <RasterSymbolizer>
            <Opacity>1.0</Opacity>
            <ColorMap>
              <ColorMapEntry color="#FFFFFF" opacity="0.0001" quantity="0" label="&lt; 0.001%" />
              <ColorMapEntry color="#66FF66" quantity="0.001" label="0.01%" />
              <ColorMapEntry color="#66CC66" quantity="0.002" label="0.02%" />
              <ColorMapEntry color="#339933" quantity="0.005" label="0.05%" />
              <ColorMapEntry color="#FFCC33" quantity="0.025" label="2.5%" />
              <ColorMapEntry color="#FF9933" quantity="0.05" label="5%" />
              <ColorMapEntry color="#FF6633" quantity="0.1"  label="10%" />
              <ColorMapEntry color="#FF3333" quantity="0.15" label="15%" />
              <ColorMapEntry color="#FF3333" quantity="0.20" label="20%" />     
              <ColorMapEntry color="#993333" quantity="0.25" label="25%" />    
              <ColorMapEntry color="#990033" quantity="0.30" label="30%" />     
              <ColorMapEntry color="#660033" quantity="0.35" label="35%" />   
              <ColorMapEntry color="#330066" quantity="0.40" label="40%" />     
            </ColorMap>
          </RasterSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>